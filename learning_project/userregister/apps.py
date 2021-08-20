from django.apps import AppConfig


class UserregisterConfig(AppConfig):
    name = 'userregister'

    def ready(self):
        import userregister.signals