# 外部引用
from os.path import join as osPathJoin
import more_itertools as mit
import json
# 內部引用
from GlobalsData import FilePathGlobals
from Model.OsFunction.OsFileModel import CheckFile

# 初始化全域變數
FilePathGlobals.initialize()


def HistoryDataLoad():
    post_list_history = []
    # img_list_history = []
    # comments_list_history = []

    if FilePathGlobals.repeat == False:
        post_list_path = osPathJoin(FilePathGlobals.dataSavePath,
                                    FilePathGlobals.post_list_file_name)

        # img_list_path = osPathJoin(FilePathGlobals.dataSavePath,
        #                            FilePathGlobals.img_list_file_name)

        # comments_list_path = osPathJoin(FilePathGlobals.dataSavePath,
        #                                 FilePathGlobals.comments_list_file_name)

        # 確認檔案是否存在
        if CheckFile(post_list_path):
            with open(post_list_path,
                      encoding='utf-8',
                      errors='ignore') as f:
                post_list_history = json.load(f, strict=False)

        # # 確認檔案是否存在
        # if CheckFile(img_list_path):
        #     with open(img_list_path,
        #               encoding='utf-8',
        #               errors='ignore') as f:
        #         img_list_history = json.load(f, strict=False)

        #         # 確認檔案是否存在
        # if CheckFile(comments_list_path):
        #     with open(comments_list_path,
        #               encoding='utf-8',
        #               errors='ignore') as f:
        #         comments_list_history = json.load(f, strict=False)
    return post_list_history


def GetHistoryMaxIndex():
    pass
    # history_max_index = 0
    # 獲取 history_max_index
    # if FilePathGlobals.repeat == False:
    #     try:
    #         history_max_index = max(post_list_history,
    #                                 key=lambda x: x['post_index'])['post_index']
    #     except Exception as e:
    #         from traceback import format_exc
    #         print(format_exc())

    #         try:
    #             history_max_index = post_list_history[-1]['post_index']
    #         except Exception as e:
    #             from traceback import format_exc
    #             print(format_exc())


def DeleteRepeatData(post_list_new, post_list_history):
    pass

    # if repeat == False:
    #     # 從歷史資料中，以slug搜尋，是否有爬過相同文章
    #     history_data = list(
    #         filter(lambda x: x['slug'] == p['slug'], post_list_history))
    #     if 0 < len(history_data):
    #         print("已存在相同資料，略過爬取")
    #         print(history_data[0]['title'],
    #               ":",
    #               history_data[0]['slug'])
    #         print("\n")
    #         continue


def UpdateRepeatData(post_list, post_list_history):

    post_list_new = []
    # 從歷史資料中，以slug搜尋，是否有爬過相同文章
    for index, post in enumerate(post_list):
        repeatDataIndexList = list(mit.locate(
            post_list_history, pred=lambda x: x['slug'] == post['slug']))

        if len(repeatDataIndexList) > 0:
            # post有重複則更新post_list_history中的資料
            for repeatDataIndex in repeatDataIndexList:
                print(f"已存在相同資料，更新post_list_history[{repeatDataIndex}]")
                print(post_list_history[repeatDataIndex]['title'])
                print(post_list_history[repeatDataIndex]['url'])
                print("\n")
                post_list_history[repeatDataIndex] = post
        else:
            # post沒有重複則加入post_list_new
            post_list_new.append(post)

    return post_list_new, post_list_history
