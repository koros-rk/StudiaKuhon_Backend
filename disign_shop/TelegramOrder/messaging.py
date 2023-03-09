import requests
from StudiaKuhon_Backend.settings import TOKEN


def send_telegram(text: str):
    token = TOKEN
    url = "https://api.telegram.org/bot"
    channel_id = "-1001607111458"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")
