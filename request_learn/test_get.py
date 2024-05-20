import requests

def test_r():
    r = requests.get('https://api.github.com/events')
    print(r.text)
    print(r.json())
    print(r.status_code)