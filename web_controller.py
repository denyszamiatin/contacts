from flask import Flask, render_template, request
import redis_phones

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')
	self.con.
    
@app.route('/set', methods=['POST',])
def set():
    return render_template(
        'set.html', 
        name=request.form.get('name', ''),
        phone=request.form.get('phone', ''),
    )

    
    
if __name__ == '__main__':
    app.run(debug=True)
