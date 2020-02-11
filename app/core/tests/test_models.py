from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

	def test_create_user_with_email_successful(self):
		"""Test creating a new user with an email is successful"""
		email = "dog@googley.com"
		password = "dogdogcatcat"
		user = get_user_model().objects.create_user(
			email = email,
			password = password,
		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_new_user_email_normalize(self):
		"""Test email for a new user is normalzied"""

		email = "dog@GOOGLEY.com"
		user = get_user_model().objects.create_user(email, "password123")

		self.assertEqual(user.email, email.lower())

	def test_new_user_invalid_email(self):
		"""Test creating user with no email raises error"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, "password123")

	def test_create_new_superuser(self):
		"""Test creating new superuser"""
		user = get_user_model().objects.create_superuser('test@googley.com', 'password123')
		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)


