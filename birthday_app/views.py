from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from jdatetime import date
import ghasedakpack
from .models import Person, BirthdayMessage
 
# Create your views here.

@csrf_exempt
def send_birthday_message():
    pass
