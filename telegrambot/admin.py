from django.contrib import admin

from .models import TelegramSettings


class TelegramBotAdmin(admin.ModelAdmin):
    list_display = ('id', 'tg_chat', 'tg_message')
    list_editable = ('tg_message', 'tg_chat')


admin.site.register(TelegramSettings, TelegramBotAdmin)