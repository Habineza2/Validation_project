from django.apps import AppConfig


class ValidationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'validationApp'




from django.apps import AppConfig

class validationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'yourapp'

    def ready(self):
        import validationApp.signals
