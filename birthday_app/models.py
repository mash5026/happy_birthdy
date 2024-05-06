from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(verbose_name='نام', max_length=100)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=100)
    date_of_birth = jmodels.jDateField(verbose_name='تاریخ تولد')
    activity_unit = models.CharField(verbose_name='واحد', max_length=100)
    specilization = models.CharField(verbose_name='تخصص', max_length=100)
    mobile_number = models.CharField(verbose_name='شماره همراه', max_length=12)
    ad_date_of_birth = models.DateField(verbose_name='تاریخ تولد میلادی', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            # Convert the Jalali date to an AD (Gregorian) date
            ad_date = self.date_of_birth.togregorian()
            self.ad_date_of_birth = ad_date.strftime('%Y-%m-%d')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name


class BirthdayMessage(models.Model):
    month_of_birth = models.IntegerField()
    message = models.TextField()
