from flask import Flask, render_template, request


app = Flask(__name__)



mail  = Mail(app)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.html')

#@app.route('/contact', methods=['POST'])


if __name__ == '__main__':
	app.run(debug=True)