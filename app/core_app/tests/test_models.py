from django.test import TestCase
from django.contrib.auth import get_user_model
from core_app import models


def sample_user(email='gustavuka@testemail.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_sucessfull(self):
        """Test that creating a new user with an email is sucessfull"""
        email = 'test@gustavuka.com'
        password = 'tesTpass321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test that the email for a new user is normalized"""
        email = 'test@GusTAVuKA.cOm'
        user = get_user_model().objects.create_user(email, 'asiojfoas')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'asdsa123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'gustavo@gustavuka.com',
            'asdfg123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
