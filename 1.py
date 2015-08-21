from flask import Flask
app = Flask(__name__)

#@app.route('/')
@app.route('/index')
def index():
        return '''<!doctype html1>
			<html>
			<head>
				<title>MyApp</title>
			</head>
				<body>
				<h1> Hello!</h1>
				<p>Text</p>
				</body>
				</body>
			</html>
		'''
if __name__ == '__main__':
        app.run(debug=True)

