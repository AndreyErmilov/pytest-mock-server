import os
import threading
from typing import Optional, Dict, Callable, Any

from flask import Flask, jsonify, request

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


def start_server():
    thread = threading.Thread(target=app.run, daemon=True)
    thread.start()
    return thread


def pytest_configure(config):
    config.addinivalue_line('markers', 'server: mark test to run mock server')


def pytest_runtest_setup(item):
    markers = list(item.iter_markers('server'))
    if len(markers) > 0:
        os.environ['WERKZEUG_RUN_MAIN'] = 'true'
        for marker in markers:
            add_route(*marker.args, **marker.kwargs)
        start_server()
