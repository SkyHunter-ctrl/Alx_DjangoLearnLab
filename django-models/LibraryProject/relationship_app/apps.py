from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
# task 3. Implement Role-Based Access Control in Django
def ready(self):
    import relationship_app.signals
    
