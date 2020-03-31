import pytest


def start_server(url: str, response: str, method: str = 'GET') -> None:
    import threading
    from flask import Flask, jsonify, request
    app = Flask(__name__)

    @app.route(url, methods=[method])
    def handler():
        return jsonify(response)

    threading.Thread(target=app.run, daemon=True).start()


def pytest_runtest_setup(item):
    marker = item.get_closest_marker('server')
    if marker is not None:
        start_server(*marker.args, **marker.kwargs)
