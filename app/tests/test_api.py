from fastapi.testclient import TestClient

from ..main import app
from ..utils import generate_shortcode

client = TestClient(app)


url = "https://www.google.com"
shortcode = generate_shortcode(url)


def test_create_new_shortcode():
    """Assert that generate a shortcode from the url
    and save it to the database
    """
    response = client.post("/", json={"url": url})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "url": url, "shortcode": shortcode}


def test_create_shortcode_with_existing_url():
    """Assert that if a URL exists in the database, return it"""
    response = client.post("/", json={"url": url})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "url": url, "shortcode": shortcode}


def test_create_shortcode_with_bad_url():
    """Asserts that it isn't possible to generate a shortcode if the url is wrong"""
    url = "bad_url"
    response = client.post("/", json={"url": url})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "invalid or missing URL scheme",
                "type": "value_error.url.scheme",
            }
        ]
    }


def test_get_url_by_shortcode():
    """Assert get url by shortcode"""
    response = client.get(f"/{shortcode}")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "url": url, "shortcode": shortcode}


def test_get_url_by_shortcode_that_doesnt_exist():
    """Assert return 404 error if shortcode does not exist"""
    response = client.get(f"/nasnd9wj")
    assert response.status_code == 404
    assert response.json() == {"detail": "Shortener not found"}
