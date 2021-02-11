from flask import Flask, render_template, request, redirect, flash
import csv

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
				flash("Please enter your email address.", "alert")
				return redirect(request.url)
			if not request.form.get('subject'):
				flash("Please enter a subject.", "alert")
				return redirect(request.url)
			if len(request.form.get('message').strip()) < 10:
				flash("Message needs to be at least 10 characters long", "alert")
				return redirect(request.url)


			data = request.form.to_dict()

			#.txt database
			# with open('db.txt', 'a') as file:
			# 	file.write(f'Email: {data["email"]}\nSubject: {data["subject"]}\nMessage: {data["message"]} \n\n\n')
 
			#csv database
			with open('db.csv', 'a', newline='') as file:
				writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
				writer.writerow([data["email"],data["subject"],data["message"]])

			flash("Message sent succesfully!", "success")
			return redirect(request.url)
	else:
		return redirect('/contact.html')

