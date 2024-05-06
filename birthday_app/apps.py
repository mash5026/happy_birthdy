from django.apps import AppConfig


class BirthdayAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'birthday_app'

    def ready(self):
        from birthday_app.scheduler import start
        start()