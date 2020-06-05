import requests
from bs4 import BeautifulSoup

def get_html(url, params=None):
    """get_html
    url:データを取得するサイトのURL
    [params]:検索サイトのパラメーター {x: param}
    """
    try:
        #データ取得
        resp = requests.get(url params=params)
        #要素の抽出
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup
    except Exception as e:
        return None


try:
    #urlを代入
    search_url = "https://www.google.co.jp/search"
    search_params = {"q": "python"}
    
    #データ取得
    soup = get_html(search_url, search_params)
    if soup != None:
        print(soup.title)
    else:
        print("取得できませんでした")
    
except: Exception as e:
    print("エラーになりました")