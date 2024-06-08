from main import app


def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test2():
    response = app.test_client().get("/base")
    assert response.status_code == 200
