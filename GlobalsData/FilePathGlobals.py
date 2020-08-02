from os import getcwd as osGetcwd
from os.path import join as osPathJoin


def initialize():
    global dataSavePath, post_list_file_name, img_list_file_name, comments_list_file_name, repeat

    dataSavePath = osPathJoin(osGetcwd(), 'CrawlerDataFile')
    post_list_file_name = "post_list.json"
    img_list_file_name = "img_list.json"
    comments_list_file_name = "comments_list.json"
    repeat = False
