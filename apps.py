from django.apps import AppConfig


class WebfunctionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webfunction'

    def ready(self):
        import webfunction.signals
