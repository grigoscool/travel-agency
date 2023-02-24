import requests
import sys
sys.path.append('.')

from .models import TelegramSettings


def send_telegram_message(tg_name, tg_phone):
    """
    Send order mail
    :return: None
    """
    setting = TelegramSettings.objects.get(pk=1)
    token = str(setting.tg_token)
    chat_id = str(setting.tg_chat)
    msg = f'{str(setting.tg_message)} \n имя: {tg_name} \n телефон: {tg_phone}'

    api = 'https://api.telegram.org/bot'
    method = '/sendMessage'
    url = api + token + method
    res = requests.post(url, data={'chat_id': chat_id, 'text': msg})



