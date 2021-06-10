# Rancher Webhook for Telegram

import os
from flask import Flask, request, jsonify
import telegram

app = Flask(__name__)


TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', None)
TELEGRAM_CHATID = os.environ.get('TELEGRAM_CHATID', None)


@app.route("/webhook", methods=["POST"])
def webhook():
    events = request.get_json()
    try:
       events[0]["labels"]["test_msg"] == "Webhook setting validated"
       return jsonify(message="Handling message"), 200
    except:
        for event in events['alerts']:
            telegram_handle(message=event['labels'])
        return jsonify(message="Handling message"), 200




def telegram_handle(message):
    if TELEGRAM_TOKEN and TELEGRAM_CHATID:
        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        text = "```{}```".format(message)
        text = text.replace(", ", "\n")
        try:
            bot.send_message(chat_id=TELEGRAM_CHATID,
                             text=text,
                             parse_mode=telegram.ParseMode.MARKDOWN,
                             timeout=int(60))
            return True
        except Exception as e:
            print(str(e))        
    else:
        return False

if __name__ == '__main__':
    app.run(host="0.0.0.0")
