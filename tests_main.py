import unittest
from unittest.mock import MagicMock
from sqlmodel import Session, select
from database import get_session
from main import Users
from fastapi.testclient import TestClient
from main import app


class GetUsersAll(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_get_users_with_data(self):
        mock_session = MagicMock(spec=Session)
        mock_users = [Users(user_id=1, user_name="Paul", department="Customers", age=19),
                      Users(user_id=2, user_name="Samuel", department="Office", age=55)]
        mock_session.exec.return_value.all.return_value = mock_users

        # to override get_session
        app.dependency_overrides[get_session] = lambda: mock_session
        response = self.client.get("/users")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [{"user_id": 1, "user_name": "Paul", "department": "Customers", "age": 19},
                          {"user_id": 2, "user_name": "Samuel", "department": "Office", "age": 55}])
