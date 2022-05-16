import os
import time
import threading
import urllib
from typing import Any, Callable, Dict, Optional

from flask import Flask, jsonify, request, url_for

app = Flask(__name__)


def add_route(url: str,
              response: Optional[str] = None,
              method: str = 'GET',
              response_type: str = 'JSON',
              status_code: int = 200,
              headers: Optional[Dict[str, str]] = None,
              callback: Optional[Callable[[Any], None]] = None,
              ) -> None:
    """
    Add route to app.
    :param url: the URL rule as string
    :param response: return value
    :param method: HTTP method
    :param response_type: type of response (JSON, HTML, RSS)
    :param status_code: return status code
    :param headers: return headers
    :param callback: function will be executes before response returns

    :return: Sample URL for testing
    """
    endpoint = '{url}::{method}::{status_code}'.format(
        url=url, method=method, status_code=status_code
    )

    @app.route(url, endpoint=endpoint, methods=[method])
    def handler(*args, **kwargs):
        if callback is not None:
            callback(request, *args, **kwargs)
        json_response = jsonify(response)
        if headers is not None:
            json_response.headers.update(headers)
        return json_response, status_code

    with app.app_context(), app.test_request_context():
        url = url_for(endpoint)

    return url


def start_server(**kwargs):
    thread = threading.Thread(target=app.run, daemon=True, kwargs=kwargs)
    thread.start()

def assert_server_ready(url, **settings) -> None:
    """
    Assert server is ready.

    :param url: server url returned by `url_for`
    :param port: server port, default is 5000
    """
    port = settings.get('port', 5000)
    server_ready_timeout = settings.get('server_ready_timeout', 3)

    url = "http://localhost:{port}{url}".format(port=port, url=url)

    start = time.time()

    while True:
        try:
            urllib.request.urlopen(url)
            break
        except urllib.error.URLError:
            if time.time() - start > server_ready_timeout:
                raise TimeoutError(f"Server is not ready in {server_ready_timeout} seconds. Please check your server_settings.")
            time.sleep(0.1)


def pytest_configure(config):
    config.addinivalue_line('markers', 'server: mark test to run mock server')


def pytest_runtest_setup(item):
    markers = list(item.iter_markers('server'))
    settings = next(item.iter_markers('server_settings'), None)
    settings = settings.kwargs if settings else {}
    if len(markers) > 0:
        os.environ['WERKZEUG_RUN_MAIN'] = 'true'
        urls = []
        for marker in markers:
            url = add_route(*marker.args, **marker.kwargs)
            urls.append(url)
        start_server(**settings)
        for url in urls:
            assert_server_ready(url, **settings)
