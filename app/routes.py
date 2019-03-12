from app import app

@app.route('/')
@app.route('/index')
def indedx():
	return 'Hello, world!'