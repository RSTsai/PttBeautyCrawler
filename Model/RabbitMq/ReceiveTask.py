from DataStructure.TaskTypeEnum import TaskTypeEnum
import pika
import json
from DataStructure.CrawlerTaskInfo import CrawlerTaskInfo
import Model.Crawler.PttBeautyCrawlerModel as PttBeautyCrawler
# import Model.Crawler.DcardBeautyCrawlerModel as DcardBeautyCrawler


# 定義回呼函數
def callback(ch, method, properties, body):
    print(f"Received body:{body}")
    taskInfoJson = json.loads(body)
    taskInfo = CrawlerTaskInfo()
    taskInfo.__dict__ = taskInfoJson

    if taskInfo.TaskType == TaskTypeEnum.PttBeauty:
        PttBeautyCrawler.CrawlerAction()
    elif taskInfo.TaskType == TaskTypeEnum.DcardBeauty:
        DcardBeautyCrawler.Action()


def ReceiveCrawlerTask():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    # 建立一個 queue
    channel.queue_declare(queue='hello')

    # 接收訊息
    channel.basic_consume('hello',
                          callback,
                          auto_ack=True)

    # 最後進入一個無窮迴圈，等待訊息。
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
