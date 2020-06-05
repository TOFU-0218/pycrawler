import requests
from bs4 import BeautifulSoup

#User-Agent
user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100"

def get_html(url, params=None,headers=None):
    """get_html
    url:データを取得するサイトのURL
    [params]:検索サイトのパラメーター {x: param}
    [headers]:ユーザーエージェント
    """
    try:
        #データ取得
        resp = requests.get(url,params=params,headers=headers)
        #要素の抽出
        soup = BeautifulSoup(resp.text, "html.parser")
        return soup
    except Exception as e:
        return None

def get_search_url(word, engine="google"):
    """get_search_url
    word: 検索するワード
    [engine]: 使用する検索サイト（デフォルトは google）
    """
    try:
        if engine == "google":
            #google 検索
            search_url = "https://www.google.co.jp/search"
            search_params = {"q": "python"}
            search_headers = {"User-Agent": user_agent}
            #データ取得
            soup = get_html(search_url, search_params, search_headers)
            if soup != None:
                tags = soup.select(".r > a")
                urls = [tag.get("href") for tag in tags]
                return urls
            else:
                return None
        else:
            return None
    except Exception as e:
        return None


try:
    result = get_search_url("python")
    if result != None:
        for url in result:
            print(url)
    else:
        print("取得できませんでした")
except Exception as e:
    print("エラーになりました")