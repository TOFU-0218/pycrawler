import time
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

class Scraper:
    """ Scraper
    get_robot_txt(url) : robots.txt の中身を精査
        url: robots.txt を確認するサイトURL
        return True, False
    get_html(url, params=None, headers=None) : サイトの情報を取得
        url: データを取得するサイトのURL
        [params]: 検索サイトのパラメーター {x: param}
        [headers]: カスタムヘッダー情報
    """
    
    @classmethod
    def get_robots_text(cls,url):
        """get_robots_txt
        url: robots.txt を確認するサイトURL
        """
        try:
            rp = RobotFileParser()
            # robots の url 取得
            parsed_url = urlparse(url)
            robots_url = "{0.scheme}://{0.netloc}/robots.txt".format(parsed_url)
            # robots.txt 取得
            rp.set_url(robots_url)
            rp.read()
            # 取得していいか確認
            return rp.can_fetch("*",url)
        except:
            return False

    @classmethod
    def get_html(cls,url, params=None,headers=None):
        """get_html
        url:データを取得するサイトのURL
        [params]:検索サイトのパラメーター {x: param}
        [headers]:ユーザーエージェント
        """
        try:
            #待機
            time.sleep(3)
            #データ取得
            resp = requests.get(url,params=params,headers=headers)
            resp.encoding = resp.apparent_encoding
            #要素の抽出
            soup = BeautifulSoup(resp.text, "html.parser")
            return soup
        except Exception as e:
            return None