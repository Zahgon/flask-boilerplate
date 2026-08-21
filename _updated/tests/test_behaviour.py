"""Behaviour tests for the migrated FastAPI application.

These exercise the observable HTTP behaviour of every route the original
Flask application exposed, verifying that each page still returns 200 and
renders its expected content after the Flask -> FastAPI migration. They use
the same ``TestClient`` helper as the unit test, so ``rv.data`` yields the
decoded response body exactly as the original suite expected.
"""

from .helpers import TestCase


class TestBehaviour(TestCase):
    def test_home_page_renders(self):
        rv = self.client.get('/')
        assert rv.status_code == 200
        assert "Sticky footer with fixed navbar" in rv.data

    def test_about_page_renders(self):
        rv = self.client.get('/about')
        assert rv.status_code == 200
        assert "About Page" in rv.data

    def test_login_page_renders_form(self):
        rv = self.client.get('/login')
        assert rv.status_code == 200
        # WTForms renders the username field and the submit control.
        assert 'name="name"' in rv.data
        assert 'type="submit"' in rv.data

    def test_register_page_renders_form(self):
        rv = self.client.get('/register')
        assert rv.status_code == 200
        # Registration exposes username and email fields.
        assert 'name="name"' in rv.data
        assert 'name="email"' in rv.data

    def test_forgot_page_renders_form(self):
        rv = self.client.get('/forgot')
        assert rv.status_code == 200
        # Forgot-password exposes the email field.
        assert 'name="email"' in rv.data

    def test_unknown_route_returns_404(self):
        # The migrated app returns a 404 for unmapped paths, preserving the
        # original Flask 404 behaviour at the status-code level.
        rv = self.client.get('/this-route-does-not-exist')
        assert rv.status_code == 404
