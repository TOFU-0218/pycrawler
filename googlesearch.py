import requests
from bs4 import BeautifulSoup

#User-Agent
user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100"

def get_html(url, params=None,headers=None):
    """get_html
    url:データを取得するサイトのURL
    [params]:検索サイトのパラメーター {x: param}
    """
    try:
        #データ取得
        resp = requests.get(url,params=params,headers=headers)
        #要素の抽出
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup
    except Exception as e:
        return None


try:
    #urlを代入
    search_url = "https://www.google.co.jp/search"
    search_params = {"q": "python"}
    search_headers = {"User-Agent": user_agent}
    #データ取得
    soup = get_html(search_url, search_params,search_headers)
    if soup != None:
        tags = soup.select(".r > a")
        for tag in tags:
            print(tag.get("href"))
    else:
        print("取得できませんでした")
    
except Exception as e:
    print("エラーになりました")