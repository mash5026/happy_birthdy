from apscheduler.schedulers.background import BackgroundScheduler
#from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone
from .utils import send_birthday_messages
from pytz import utc
from apscheduler.triggers.cron import CronTrigger

def start():
    scheduler = BackgroundScheduler(timezone=utc)
    #scheduler.add_jobstore(DjangoJobStore(), "default")

    # Schedule the job to run daily at 16:00
    scheduler.add_job(
        send_birthday_messages,
        trigger=CronTrigger(
        hour=10,
        minute=49      
    ),)
    scheduler.start()