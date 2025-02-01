import requests

def test_rest_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

if __name__ == '__main__':
    test_api()
