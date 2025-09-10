from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
    def ready(self): # # Task 3 connecting sinals.py to app.py
    import relationship_app.signals
    

