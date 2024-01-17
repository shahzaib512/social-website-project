from django.contrib import admin
from .models import Action

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['verb', 'user', 'target', 'created']
    list_filter = ['created']
    search_fields = ['verb']
