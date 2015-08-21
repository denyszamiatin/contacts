from flask import Flask, render_template, request,redirect
import redis_phones

app = Flask(__name__)
contacts= redis_phones.Contacts(None)

@app.route('/index')
def index():
    return render_template('index.html',c=contacts.list_contacts())

@app.route('/set', methods=['POST',])
def set():
	try:
    		contacts.add_contact(request.form.get('name',''),request.form.get('phone',''))
	except KeyError as e:
		Warning=str(e)
   	return redirect(
        'index'
    )
@app.route('/create',methods = ['GET','POST'])
def create():
	if request.method == 'GET':
		return 	render_template('create.html')
	try:
		contacts.add_contact(request.form.get('name',''),request.form.get('phone',''))
	except KeyError as e:
		return render_template('create.html', warning=str(e),name=request.form.get('name',''),phone=request.form.get('phone',''))


if __name__ == '__main__':
    app.run(debug=True)

