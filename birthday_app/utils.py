from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from jdatetime import date
import ghasedakpack
from .models import Person, BirthdayMessage
 
# Create your views here.


def send_birthday_messages():
    sms = ghasedakpack.Ghasedak('5c793190795688a7a6b73842629ee2815f3249a57c5bd66f31a7648741804616')    
    today = timezone.now().astimezone().date()
    today_jalali = date.fromgregorian(date=today)
    month = today_jalali.month
    print(month)
    days = today_jalali.day
    print(days)
    birthday_messages = BirthdayMessage.objects.get(month_of_birth=month)
    persons = Person.objects.all()

    for person in persons:        
        if person.date_of_birth.day == days and person.date_of_birth.month == month:
            print(person)
            sms.send({'message': birthday_messages.message, 'receptor' : person.mobile_number, 'linenumber': '30005006009351' })