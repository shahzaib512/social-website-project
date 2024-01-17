from django.contrib.contenttypes import ContentType
from .models import Action 

def create_action(user, verb, target=None):
    action = Action(user=user, verb=verb, target=target)
    action.save()
    