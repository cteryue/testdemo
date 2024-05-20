import pytest
import requests
import yaml

from utils.get_data import get_data


@pytest.mark.parametrize("shouji,appkey", get_data()['mobile_params'])
def test_params(shouji,appkey):
    # with open("..//config//test01.yaml", encoding="utf-8") as f:
    #     data = yaml.safe_load(f)
    # params = data["params"]
    print(shouji,appkey)
    r = requests.post("http://sellshop.5istudy.online/sell/shouji/query",
                      params={"shouji": shouji,"appkey" : appkey})

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
