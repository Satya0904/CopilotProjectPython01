import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_about_route(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the about page."}
    def test_add_msg_route(client):
        response = client.post("/messages/HelloWorld/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert data["message"]["msg_name"] == "HelloWorld"
        assert isinstance(data["message"]["msg_id"], int)

    def test_message_items_route(client):
        # Add two messages
        client.post("/messages/FirstMsg/")
        client.post("/messages/SecondMsg/")
        response = client.get("/messages")
        assert response.status_code == 200
        data = response.json()
        assert "messages:" in data
        # There should be at least two messages
        assert len(data["messages:"]) >= 2
        # Check that the message names are correct
        msg_names = [msg["msg_name"] for msg in data["messages:"].values()]
        assert "FirstMsg" in msg_names
        assert "SecondMsg" in msg_names
        def test_add_msg(client):
            response = client.post("/messages/TestCountry/")
            assert response.status_code == 200
            data = response.json()
            assert "message" in data
            assert data["message"]["msg_name"] == "TestCountry"
            assert isinstance(data["message"]["msg_id"], int)

        def test_message_items(client):
            # Add two messages
            client.post("/messages/Alpha/")
            client.post("/messages/Beta/")
            response = client.get("/messages")
            assert response.status_code == 200
            data = response.json()
            assert "messages:" in data
            # There should be at least two messages
            assert len(data["messages:"]) >= 2
            # Check that the message names are correct
            msg_names = [msg["msg_name"] for msg in data["messages:"].values()]
            assert "Alpha" in msg_names
            assert "Beta" in msg_names