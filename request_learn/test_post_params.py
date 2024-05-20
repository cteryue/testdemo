import requests

def test_params():

    params = {
        "shouji": "15618919441",
        "appkey": "0c818521d38759e1"
    }

    r = requests.post("http://sellshop.5istudy.online/sell/shouji/query", params=params)

    print(r.text)
    print(r.json())
    print(r.status_code)
    assert r.status_code == 200
    rp = r.json()
    assert rp["status"] == 0
    assert rp["msg"] == "ok"
    assert rp["result"]["shouji"] == "15618919441"
    assert rp["result"]["province"] == "上海"
    assert rp["result"]["city"] == "上海"
    assert rp["result"]["company"] == "中国联通"
    assert rp["result"]["areacode"] == "0571"
