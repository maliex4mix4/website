from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(dict(
	DEBUG =True,
	MAIL_SERVER = 'smtp.gmail.com',
	MAIL_PORT = 587,
	MAIL_USE_TLS = True,
	MAIL_USE_SSL =False,
	MAIL_USERNAME = '',
	MAIL_PASSWORD = '',
))

mail  = Mail(app)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
	email = request.form['email']
	name = request.form['name']
	subject = request.form['subject']
	body = request.form['message']

	msg = Message(subject, sender=email, recipients=['malikopeyemi5@gmail.com'])
	msg.body = body
	if (mail.send(msg)):
		return 'OK'
	else:
		return 'Mail not sent. Try again'

if __name__ == '__main__':
	app.run(debug=True)