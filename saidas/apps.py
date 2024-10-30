from django.apps import AppConfig


class SaidasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'saidas'

    def ready(self):
        import saidas.signals