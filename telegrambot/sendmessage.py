import logging
import requests
import sys

sys.path.append('.')

from .models import TelegramSettings

logger = logging.getLogger(__name__)


def send_telegram_message(tg_name, tg_phone):
    """
    Send order mail
    :return: None
    """
    if TelegramSettings.objects.get(pk=1):
        setting = TelegramSettings.objects.get(pk=1)
        token = str(setting.tg_token)
        chat_id = str(setting.tg_chat)

        msg = f'{str(setting.tg_message)} \n имя: {tg_name} \n телефон: {tg_phone}'

        api = 'https://api.telegram.org/bot'
        method = '/sendMessage'
        url = api + token + method

        try:
            res = requests.post(url, data={'chat_id': chat_id, 'text': msg})

        except:
            pass

        finally:
            if res.status_code != 200:
                logger.warning('Наша ошибка')
            elif res.status_code == 500:
                logger.warning('Ошибка серверa')
            else:
                logger.info('Сообщение отправлено')

    else:
        pass
