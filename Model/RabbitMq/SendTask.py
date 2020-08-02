
from DataStructure.CrawlerTaskInfo import CrawlerTaskInfo
from DataStructure.TaskTypeEnum import TaskTypeEnum
import pika
import json
# import sys


def SendCrawlerTask():
    # 連接到 broker（RabbitMQ 伺服器）
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    #  創建對象
    channel = connection.channel()

    # 建立任務資料
    taskInfo = CrawlerTaskInfo()
    taskInfo.TaskType = TaskTypeEnum.PttBeauty
    taskInfo.Count = 10
    taskInfo.BreakTime = 10

    # 建立一個 queue
    channel.queue_declare(queue='hello')

    # 發送訊息
    channel.basic_publish(exchange='',  # 交換機
                          routing_key='hello',  # 指定的隊列名稱
                          body=json.dumps(taskInfo.__dict__))  # 值

    print(" [x] Sent 'Hello World!")

    # 關閉連線
    connection.close()
