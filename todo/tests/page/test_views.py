from flask import url_for

import re


class TestPage(object):
    def tests_home_page(self, client):
        """Home page should respond with a successful 200 response."""
        response = client.get(url_for('page.home'))
        assert response.status_code == 200
        regexp = re.compile('<title>.+</title>')
        assert regexp.search(response.get_data(as_text=True))

    def test_terms_page(self, client):
        """Terms page should respond with a successful 200 response"""
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200
        regexp = re.compile('<title>.+</title>')
        assert regexp.search(response.get_data(as_text=True))

    def test_privacy_page(self, client):
        """Privacy page should respond with a successful 200 response"""
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200
        regexp = re.compile('<title>.+</title>')
        assert regexp.search(response.get_data(as_text=True))

    def test_faq_page(self, client):
        """FAQ page should respond with a successful 200 response"""
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200
        regexp = re.compile('<title>.+</title>')
        assert regexp.search(response.get_data(as_text=True))
