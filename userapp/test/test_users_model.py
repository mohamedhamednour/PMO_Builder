from userapp.factories import UserFactory
from rest_framework.test import APITestCase


from userapp.factories import UserFactory
from rest_framework.test import APITestCase


class NormalUserTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory(
            email="hamed@gmail..com",
            first_name="mohamed",
            last_name="hamed",
            is_superuser=False,
            is_staff=False,
        )

    def test_user_creation(self):
        assert self.user.email == "hamed@gmail..com"
        assert self.user.first_name == "mohamed"
        assert self.user.last_name == "hamed"
        assert self.user.check_password("password123")

    def test_user_is_active(self):
        assert self.user.is_active

    def test_user_is_not_superuser(self):
        assert not self.user.is_superuser

    def test_user_is_not_staff(self):
        assert not self.user.is_staff


class SuperUserTestCase(APITestCase):
    def setUp(self):
        self.superuser = UserFactory(
            email="admin@example.com",
            first_name="mo",
            last_name="nour",
            is_superuser=True,
            is_staff=True,
        )

    def test_superuser_creation(self):
        assert self.superuser.email == "admin@example.com"
        assert self.superuser.is_superuser
        assert self.superuser.is_staff
        assert self.superuser.check_password("password123")
