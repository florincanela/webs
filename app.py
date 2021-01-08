from flask import Flask, render_template, request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/<string:route>')
def function(route):		
	return render_template(route)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
	if request.method == 'POST':
			if not request.form.get('email'):
				return "Please enter an email address"
			if not request.form.get('subject'):
				return "Please enter a subject."
			if len(request.form.get('message').strip()) < 10:
				return "Message needs to be at least 10 characters long"

			data = request.form.to_dict()

			#.txt database
			# with open('db.txt', 'a') as file:
			# 	file.write(f'Email: {data["email"]}\nSubject: {data["subject"]}\nMessage: {data["message"]} \n\n\n')
 
			#csv database
			with open('db.csv', 'a', newline='') as file:
				writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				writer.writerow([data["email"],data["subject"],data["message"]])


			return redirect('/')
	else:
		return redirect('/contact.html')

