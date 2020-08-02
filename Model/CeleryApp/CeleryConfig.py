from datetime import timedelta
from celery.schedules import crontab


# 使用RabbitMQ作為消息代理
BROKER_URL = 'amqp://'
# broker_url = 'amqp://guest:guest@localhost:5672//'
# 任務結果儲存位置
# CELERY_RESULT_BACKEND = 'amqp://'
# 任務序列化和反序列化使用JSON方案
# CELERY_TASK_SERIALIZER = 'json'
# 讀取任務結果使用JSON
# CELERY_RESULT_SERIALIZER = 'json'
# 任務過期時間，不建議直接寫86400，應該讓這樣的magic數字表述更明顯
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
# 指定接受的內容類型，是一個副本，可以寫多個
# CELERY_ACCEPT_CONTENT = ['json']


# # Timezone
# CELERY_TIMEZONE = 'Asia/Shanghai'    # 指定時區，不指定默认為 'UTC'

# import
CELERY_IMPORTS = (
    'Model.CeleryApp.CeleryTask'
)


# schedules
CELERYBEAT_SCHEDULE = {
    'TestTask30sec': {
        'task': 'Model.CeleryApp.CeleryTask.PttCrawler',
        'schedule': timedelta(seconds=30),
        'args': (1, 0)
    }
    # 'PttCrawler': {
    #     'task': 'Model.Crawler.PttBeautyCrawlerModel.CrawlerAction',
    #     'schedule': timedelta(seconds=30),
    #     'args': (1)
    # }
}
