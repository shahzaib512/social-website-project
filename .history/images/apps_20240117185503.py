from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
    
    def ready(self):
        # import signla handlers
        import images.signals
        
