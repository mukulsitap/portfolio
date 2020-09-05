from flask import Flask, flash, redirect, render_template, \
     request, url_for
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template('./index.html')

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["msg"]
		file = database.write(f'\n{name}, {email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', mode='a') as database2:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["msg"]
		csv_writer = csv.writer(database2, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name, email, subject, message])

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_f():
    if request.method == 'POST' :
    	data = request.form.to_dict()
    	write_to_file(data)
    	write_to_csv(data)
    	print(data)
    	
    	return redirect('index2.html')
    else:
    	return 'try again'


@app.route('/index2.html')
def home_page2():
    return render_template('./index2.html')
