from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserTests(APITestCase):
	def setUp(self):
		User.objects.create_user('admin', 'admin@admin.com', 'vulpecula')

	def test_get_user(self):
		self.client.login(username='admin', password='vulpecula')
		response = self.client.get('/users/', format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.client.logout()