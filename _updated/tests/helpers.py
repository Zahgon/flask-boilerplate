import unittest

from fastapi.testclient import TestClient as _StarletteTestClient

from app import create_app


class _Response(object):
    """Wrap a Starlette/httpx response so ``.data`` yields decoded text.

    The original Werkzeug-based helper returned ``rv.data`` as a native
    string under Python 2. On Python 3 that attribute is ``bytes``; exposing
    the decoded body here keeps ``substring in rv.data`` assertions working
    exactly as the tests were written.
    """

    def __init__(self, response):
        self._response = response

    @property
    def data(self):
        return self._response.text

    @property
    def status_code(self):
        return self._response.status_code


class TestClient(object):
    def __init__(self, app):
        self.app = app
        self.client = _StarletteTestClient(app)

    def get(self, url, headers=None):
        return _Response(self.client.get(url, headers=headers or {}))

    def post(self, url, data=None, headers=None):
        return _Response(
            self.client.post(url, json=data, headers=headers or {})
        )

    def put(self, url, data=None, headers=None):
        return _Response(
            self.client.put(url, json=data, headers=headers or {})
        )

    def delete(self, url, headers=None):
        return _Response(self.client.delete(url, headers=headers or {}))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config')
        self.client = TestClient(self.app)

    def tearDown(self):
        pass
