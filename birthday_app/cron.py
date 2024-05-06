from django_cron import CronJobBase, Schedule
from .views import send_birthday_message


class SendBirthdayMessageJob(CronJobBase):
    run_every_miins = 1
    schedule = Schedule(run_every_mins=run_every_miins)
    code = 'birthday_app.send_birthday_message_job'

    def do(self):
        print('run')
        send_birthday_message()
        print('end')