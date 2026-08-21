from .helpers import TestCase


class TestPage(TestCase):
    def test_header(self):
        rv = self.client.get('/')
        assert "Sticky footer with fixed navbar" in rv.data
