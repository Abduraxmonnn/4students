from django.contrib import admin

from telegram_bot.models import TGUser


# Register your models here.

@admin.register(TGUser)
class TGUserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'created_on', 'updated_on']
    list_display_links = ['user_id', 'username']
    search_fields = ['user_id', 'username']
