import requests

token = '6142375179:AAHM3GgdrfT4iSxdko9rjgF8HJBNEhQH8ps'
chat_id = '1137542556'
text = 'Серж пишет ботофф'


def send_telegram_message():
    """
    Send order mail
    :return: None
    """
    api = 'https://api.telegram.org/bot'
    send_msg = api + token + '/sendMessage'
    req = requests.post(send_msg, data={'chat_id': chat_id, 'text': text})


send_telegram_message()
