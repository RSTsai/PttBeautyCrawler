from __future__ import absolute_import
from celery import Celery


app = Celery('CrawlerCelery')
app.config_from_object('Model.CeleryApp.CeleryConfig')


'''
[CMD 啟動指令]
celery worker -A CeleryMain -l INFO
celery beat -A CeleryMain -l INFO
celery -B -A CeleryMain worker --loglevel=info
-B option does not work on Windows.  Please run celery beat as a separate service.

pip uninstall celery
pip install celery==4.3.0
celery beat -A CeleryMain -l INFO
celery worker -A CeleryMain --pool=solo -l INFO

'''
