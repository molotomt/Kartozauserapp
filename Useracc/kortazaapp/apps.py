from django.apps import AppConfig


class KortazaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kortazaapp'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import kortazaapp.signals
