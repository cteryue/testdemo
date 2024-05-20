import requests


def test_params():
    form_data = {
        "text": "测试",
    }

    r = requests.post("https://dict.youdao.com/keyword/key", data=form_data)

    print(r.text)
    print(r.json())
    print(r.status_code)
    assert r.status_code == 200

