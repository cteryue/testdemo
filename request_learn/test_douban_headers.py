import requests

def test_headers():
    url = "https://movie.douban.com/j/search_subjects"
    params = {
        "type" : "movie",
        "tag" : "热门",
        "page_limit" : "page_limit",
        "page_start" : "0"
    }

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }

    r = requests.get(url=url,params = params,headers=headers)
    print(r.json())
    print(r.text)
    print(r.status_code)
    assert r.status_code == 200