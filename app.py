from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('0/yzNrSfDbKlzW71VHqihxj58Ajt/B4irPzrmf3UNZuY0+dYnlwfilPKx1GF27mScsTUqrVK3w6oZeHXIzvsejuv+Ooviy/Wb3L5RHoe4DhKVBdkJMPL5G7ybFtkUjdmwFYb45Eoe9BcaUcxHhmfrwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('02b500943a8dd6f61b75f0f1f5355201')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg=event.message.text
	r = '''Hi there, thanks for adding me as friend! I am line-bot. 
	Which information you want to know?
	(1)location
	(2)meeting time
	(3)contact window
	(4)FB Fanpage
	'''

	Location = ['Location', 'location', '1']
	Time = ['Time', 'time', 'meeting time', 'Meeting time','2']
	Contact = ['Window','window','Contact','contact', 'Contact window','contact window','3']
	FB = ['facebook', 'Facebook', 'fb', 'FB','Fanpage', 'fanpage', 'FB fanpage','FB Fanpage','4']


	if msg in Location:
		r = 'Meeting will take place at NTHU Delta Hall R601 (清華大學 台達館 601室)'

	elif msg in Time:
		r = 'Meeting will be held from 19:00 to 21:00 every Thursday'

	elif msg in Contact:
		r = 'You can contact Johnny, president of this club, for more information. LINE ID:'

	elif msg in FB:
		r = 'https://www.facebook.com/nthutoastmasters/'

	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()