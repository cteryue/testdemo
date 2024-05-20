import requests


def test_params():
    json_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    r = requests.post("https://jsonplaceholder.typicode.com/posts", json=json_data)

    print(r.text)
    print(r.json())
    print(r.status_code)
    assert r.status_code == 201

