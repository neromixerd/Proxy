from app import app
from unittest import TestCase


class TestIntegrations(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_repo(self):
        response = self.app.get(
            '/get_repo',
            content_type='multipart/form-data',
            data=dict(
                user_repo='Jays2Kings/DS4Windows'),
        )
        return self.assertEqual(response.status_code, 200)

    def test_get_pulls(self):
        response = self.app.get(
            '/get_pulls',
            content_type='multipart/form-data',
            data=dict(
                user_repo='Jays2Kings/DS4Windows'),
        )
        return self.assertEqual(response.status_code, 200)

    def test_get_unmerged_pulls(self):
        response = self.app.get(
            '/get_unmerged_pulls',
            content_type='multipart/form-data',
            data=dict(
                user_repo='Jays2Kings/DS4Windows'),
        )
        return self.assertEqual(response.status_code, 200)

    def test_get_issues(self):
        response = self.app.get(
            '/get_issues',
            content_type='multipart/form-data',
            data=dict(
                user_repo='Jays2Kings/DS4Windows'),
        )
        return self.assertEqual(response.status_code, 200)

    def test_get_forks(self):
        response = self.app.get(
            '/get_forks',
            content_type='multipart/form-data',
            data=dict(
                user_repo='Jays2Kings/DS4Windows'),
        )
        return self.assertEqual(response.status_code, 200)
