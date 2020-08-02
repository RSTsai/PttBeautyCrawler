# 外部引用
from os.path import join as osPathJoin
import json
# 內部引用
from GlobalsData import FilePathGlobals
from Model.OsFunction.OsFileModel import CheckDir
from Model.Crawler.listpage_crawler import get_post_list
from Model.Crawler.postpage_crawler import post_crawler


def CrawlerAction(days):
    try:
        # 初始化全域變數
        FilePathGlobals.initialize()

        # 取得指定天數的 post list 資料，存成陣列
        post_list_temp = get_post_list(days)
        # print("\n\n post_list:", post_list)

        # 從陣列裡面把每個 url 丟進 post_crawler 爬取 po 文內容，回傳 post_time, author, comments, img_name_list, img_url_list
        post_list = []
        # img_list = []
        # comments_list = []
        for index, post in enumerate(post_list_temp):
            post_time, author, comments, img_name_list, img_url_list = post_crawler(
                post['url'], index)

            post_list_temp[index]['post_time'] = post_time
            post_list_temp[index]['author'] = author
            post_list_temp[index]['imgs'] = img_url_list
            post_list_temp[index]['comments'] = comments
            post_list.append(post_list_temp[index])

            # # img_list
            # for imgUrl in img_url_list:
            #     imgs_dict = {}
            #     imgs_dict['post_index'] = postIndex
            #     # print(post_time, author, img_name_list, img_url_list)
            #     imgs_dict['img_url'] = imgUrl
            #     img_list.append(imgs_dict)

            # #  comments_list
            # for comment_info in comments:
            #     comments_dict = {}
            #     comments_dict = comment_info
            #     comments_dict['post_index'] = postIndex
            #     comments_list.append(comments_dict)

            # 顯示每一頁的資料
            print(post_list[index]['title'])
            print(post_list[index]['url'], '\n')

        # 確認保存資料夾是否存在
        CheckDir(FilePathGlobals.dataSavePath)

        # 從歷史數據中剔除重複資料
        from Model.Crawler.HistoryData.JsonHistoryDataModel import HistoryDataLoad, UpdateRepeatData
        post_list_history = HistoryDataLoad()
        post_list, post_list_history = UpdateRepeatData(
            post_list, post_list_history)
        post_list.extend(post_list_history)

        # 存成字典post_list
        with open(osPathJoin(FilePathGlobals.dataSavePath, FilePathGlobals.post_list_file_name),
                  'w', encoding="utf-8") as file:
            json.dump(post_list, file, ensure_ascii=False)

        # # img_list
        # with open(osPathJoin(FilePathGlobals.dataSavePath, FilePathGlobals.img_list_file_name),
        #           'w', encoding="utf-8") as file:
        #     json.dump(img_list, file, ensure_ascii=False)

        # # comments_list
        # with open(osPathJoin(FilePathGlobals.dataSavePath, FilePathGlobals.comments_list_file_name),
        #           'w', encoding="utf-8") as file:
        #     json.dump(comments_list, file, ensure_ascii=False)

    except Exception as e:
        from traceback import format_exc
        print(format_exc())
