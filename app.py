# Created on 2021-04-30 by Walter Hsieh

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
	r = '''Hi there, thanks for adding me as friend! I am a line-bot.\nWhich information you want to know?\n1 Location\n2 Meeting time\n3 Contact window\n4 FB Fan page\n5 About me\n6 Roles\n Please type the number 1,2,3...for the answer'''

	chat = {
	'7':"No, you don't need to be fluent. Here we provide friendly and English immersing evironment for you to practice.",
	'8':"Don't worry about that. Only thing you need is to come and have fun.",
	'9':'Join our regular meeting, we will help to go through the process.',
	'10':"Toastmasters is nonprofit educational organization which helps its members improve their public speaking skills and build their leadership style.",
	'11':'I am a line-bot serving for NTHU toastmasters. And you are?',
	'12':'I was first created on 2021-04-30 by Walter Hsieh. You do the math lol',
	'13':'I like to chat with people even though we have nothing to say :)'
	}


	Location = ['Location', 'location', '1']
	Time = ['Time', 'time', 'meeting time', 'Meeting time','2']
	Contact = ['Window','window','Contact','contact', 'Contact window','contact window','3']
	FB = ['facebook', 'Facebook', 'fb', 'FB','Fanpage', 'fanpage', 'FB fanpage','FB Fanpage','4']
	Me = ['About me','about me', 'me','Me','5']
	roles = ['roles','role','Role', 'Roles','TME','Timer','counter','Counter','grammarian','Grammarian','Evaluator','evaluator', '6']



	if msg in Location:
		# r = 'Meeting will take place at NTHU Delta Hall R601 (清華大學 台達館 601室)'
		# r ='Due to COVID-19, meeting will be held online at Google Meet https://meet.google.com/voh-rius-bvu'
		r ='Due to COVID-19, meeting will be held online at ZOOM (ID: 87852935032, Password: 452318) https://us02web.zoom.us/j/87852935032?pwd=NytQT0dqdjVyQ0VJdVJxRHl0VnBwdz09'

	elif msg == 'Location & Meeting Time':
		# r = 'Meeting will take place at NTHU Delta Hall R601 (清華大學 台達館 601室) from 19:00 to 21:00 every Thursday'
		# r ='Due to COVID-19, meeting will be held online at Google Meet https://meet.google.com/voh-rius-bvu'
		r ='Due to COVID-19, meeting will be held online at ZOOM (ID: 87852935032, Password: 452318) https://us02web.zoom.us/j/87852935032?pwd=NytQT0dqdjVyQ0VJdVJxRHl0VnBwdz09'
	
	elif msg in Time:
		r = 'Meeting will be held online from 19:00 to 21:00 every Thursday'

	elif msg in Contact:
		r = 'write an email to us \nnthutoastmasters@gmail.com'

	elif msg in FB:
		r = 'https://www.facebook.com/nthutoastmasters/'

	elif msg in chat.keys():
		r = chat[msg]

	elif msg in Me:
		r = 'Questions about me are listed below\n11 Who are you?\n12 How old are you?\n13 What is your hobby?\nPlease type 11, 12...for the annswer'
	
	elif msg in roles:
		r = 'https://www.toastmasters.org/membership/club-meeting-roles'

	elif msg == 'Q&A':
		r = '7 Should I speak English fluently?\n8 Should I learn any thing before I join?\n9 How to join this club?\n10 What is Toastmaster?\nPlease type 7, 8...for the annswer'


	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()