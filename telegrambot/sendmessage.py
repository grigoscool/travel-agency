import requests

from .models import TelegramSettings


def send_telegram_message():
    """
    Send order mail
    :return: None
    """
    settings = TelegramSettings.objects.get(pk=1)

    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    msg = str(settings.tg_message)

    api = 'https://api.telegram.org/bot'
    send_msg = api + token + '/sendMessage'
    req = requests.post(send_msg, data={'chat_id': chat_id, 'msg': msg})

send_telegram_message()

