import unittest
from unittest.mock import MagicMock
from DAL.user_api_connector_LAB7 import UserAPIConnector
from BLL.user_repository_LAB7 import UserRepository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.api_connector = MagicMock(spec=UserAPIConnector)
        self.user_repo = UserRepository(self.api_connector)

    def test_get_all_users(self):
        # Імітуємо повернення списку користувачів
        self.api_connector.get_users.return_value = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

        users = self.user_repo.get_all_users()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0]['name'], "John Doe")
        self.assertEqual(users[1]['name'], "Jane Smith")

    def test_get_user_posts(self):
        # Імітуємо повернення постів користувача
        self.api_connector.get_user_posts.return_value = [{"id": 1, "title": "Post 1"}, {"id": 2, "title": "Post 2"}]

        posts = self.user_repo.get_user_posts(1)
        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0]['title'], "Post 1")

    def test_get_user_by_name(self):
        # Імітуємо пошук користувача за ім'ям
        self.api_connector.get_users.return_value = [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]

        user = self.user_repo.get_user_by_name("John Doe")
        self.assertIsNotNone(user)
        self.assertEqual(user['name'], "John Doe")

        # Перевірка, якщо користувача не знайдено
        user = self.user_repo.get_user_by_name("Nonexistent User")
        self.assertIsNone(user)

