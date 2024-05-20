import pytest
import requests


class Test01:
    # 方法级始末调用（在类中的）
    def setup_method(self):
        print()
        print("准备测试数据")

    def teardown_method(self):
        print()
        print("清理测试数据")

    def test_params1(self):

        params = {
            "shouji": "15618919441",
            "appkey": "0c818521d38759e1"
        }

        r = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=params)

        # print(r.text)
        # print(r.json())
        # print(r.status_code)
        assert r.status_code == 200
        rp = r.json()
        assert rp["status"] == 0
        assert rp["msg"] == "ok"
        assert rp["result"]["shouji"] == "15618919441"
        assert rp["result"]["province"] == "上海"
        assert rp["result"]["city"] == "上海"
        assert rp["result"]["company"] == "中国联通"
        assert rp["result"]["areacode"] == "0571"

    def test_params2(self):

        params = {
            "shouji": "15618919441",
            "appkey": "0c818521d38759e1"
        }

        r = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=params)

        # print(r.text)
        # print(r.json())
        # print(r.status_code)
        assert r.status_code == 200
        rp = r.json()
        assert rp["status"] == 0
        assert rp["msg"] == "ok"
        assert rp["result"]["shouji"] == "15618919441"
        assert rp["result"]["province"] == "上海"
        assert rp["result"]["city"] == "上海"
        assert rp["result"]["company"] == "中国联通"
        assert rp["result"]["areacode"] == "0571"

if __name__ == '__main__':
    pytest.main()
