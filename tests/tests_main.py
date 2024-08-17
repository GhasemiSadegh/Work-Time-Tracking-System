import unittest
from unittest.mock import MagicMock
from sqlmodel import Session, select
from database import get_session
from main import Users
from fastapi.testclient import TestClient
from main import app


# Testing get method for users
class GetUsersAll(unittest.TestCase):

    def setUp(self):  # Prepares the environment for each test method
        self.client = TestClient(app)

    def test_get_users_with_data(self):
        mock_session = MagicMock(spec=Session)  # the mock should mimic the interface of the given class, Session
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

    def test_get_users_no_data(self):
        mock_session = MagicMock(spec=Session)
        mock_user = []
        mock_session.exec.return_value.all.return_value = lambda: mock_session
        response = self.client.get("/users")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Please add a user first. The list is empty.')


# Testing add method for a user


class AddUser(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_add_user_input_right(self):
        response = self.client.post("/users/add", json={"user_id": 1,
                                                        "user_name": "Paul",
                                                        "department": "Customers",
                                                        "age": 19}
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "New user added.")

    def test_add_user_short_name(self):
        response = self.client.post("/users/add", json={"user_id": 1,
                                                        "user_name": "Pa",
                                                        "department": "Customers",
                                                        "age": 19})

        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {
            "detail": [{"type": "string_too_short", "loc": ["body", "user_name"],
                        "msg": "String should have at least 3 characters", "input": "Pa", "ctx": {"min_length": 3}}]})


class AddSession(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_add_session(self):
        response = self.client.post("/session/add", json={"session_user": "Ali",
                                                          "session_project": "Linux",
                                                          "date": "2024-08-17",
                                                          "start_time": "17:00:52.110Z",
                                                          "end_time": "17:14:52.110Z"
                                                          }
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Session added successfully.")
        
