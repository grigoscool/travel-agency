from django.db import models


class TelegramSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='Чат')
    tg_message = models.CharField(max_length=200, verbose_name='Сообщение')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'Насстройка'
        verbose_name_plural = 'Настройки'
