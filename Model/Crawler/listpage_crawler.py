# -*- coding: utf-8 -*

import requests
from bs4 import BeautifulSoup as bs
from Model.Crawler.day_computing import get_date_str, Is_within_Target_Date_2020
from time import sleep, time


def ptt_listpage_crawler(url, day_bias=0, repeat=False, post_list_history=None):
    """
    crawl the ptt list page

    para::[url]
        - type: str
        - starting page URL
    para::[day_bias]
        - type: (minus) int
        - number of days before today
        - example: zero stands for today; -1 stands for yesterday
    return::
        - [str] url of previous page; return None if achieved target date
        - [list] posts collection with target date
    """

    jar = requests.cookies.RequestsCookieJar()
    # 可把不同網頁的 cookie 設定進一個jar
    jar.set("over18", "1", domain="www.ptt.cc")
    # 將cookies加入request
    response = requests.get(url, cookies=jar).text
    # response為html格式，交由bs4解析
    html = bs(response)

    # 找到導航列
    navi_bar = html.find("div", class_="btn-group btn-group-paging")
    navi_bottons = navi_bar.find_all("a", class_="btn wide")
    # 從導航列取得上一頁的URL(next_url)
    next_url = None
    for n in navi_bottons:
        if '上頁' in n.text:
            next_url = "https://www.ptt.cc" + n["href"]

    post_block = html.find(
        "div", class_="r-list-container action-bar-margin bbs-screen")
    posts = post_block.find_all("div", class_="r-ent")
    post_list = []
    for post in posts:
        p = {}
        # Title - 文章標題
        try:
            p['title'] = post.find("div", class_="title").find("a").text
        except AttributeError:      # 如果文章已被刪除則略過
            p['title'] = post.find("div", class_="title").text
            if '刪除' in p['title']:
                continue
        if '公告' in p['title']:    # 如果是公告文則略過
            continue

        # URL - 文章連結
        try:
            url_path = post.find("div", class_="title").find("a")["href"]
            p['url'] = "https://www.ptt.cc" + url_path
            p['slug'] = '.'.join(url_path.split('/')[3].split('.')[:4])

        except:
            continue

        # DATE - 日期
        p['post_time'] = post.find("div", class_="date").text
        if not Is_within_Target_Date_2020(p['post_time'], get_date_str(day_bias)):
            next_url = None
            continue  # 不在目標日期範圍內，略過此筆

        # PUSH - 推文數
        try:
            p['push'] = post.find("div", class_="nrec").find(
                "span", class_="hl").text
        except AttributeError:      # 處理沒有人推文
            p['push'] = 0
        post_list.append(p)

    return next_url, post_list

# # Print for debugging
# for p in post_list:
#     for key, value in p.items():
#         print("{}: {}" .format(key, value))
#     print("------------------------------------------------")


# 取得PPT每一頁上的文章資訊
def get_post_list(day_bias=7):
    '''
    取得指定天數的 post list 資料，存成陣列

    Input day_bias: 要查詢的天數(正整數)
    return msg_r : 可傳給使用者看的查詢結果(string)
    return df_r : 查詢結果組成的sorted DataFrame
    '''
    # PTT表特版首頁
    url = "https://www.ptt.cc/bbs/Beauty/index.html"

    day_bias = -day_bias + 1

    start_time = time()

    post_list = []
    delay_sec = 0.1
    count = 0
    if day_bias > 0:
        print("Check day_bias!!!")
    # while url != None:
    while url is not None:
        print("開始爬取:", url, '\n')
        url, next_post_list = ptt_listpage_crawler(
            url, day_bias)
        post_list = post_list + next_post_list[::-1]
        count += 1
        sleep(delay_sec)

    end_time = time()
    duration = end_time - start_time
    print("花費時間: ", duration, '\n')
    return post_list
