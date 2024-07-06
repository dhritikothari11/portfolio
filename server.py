from flask import Flask,render_template,request,redirect
import csv
app=Flask(__name__)

@app.route('/')
def heloo():
	return render_template('index.html')

@app.route('/<string:page_name>')
def page_name(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('databse.txt',mode='a') as database:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		file=database.write(f'{email},{subject},{message}')
def write_to_file(data):
	with open('databse.csv',mode='a',newline="") as database2:
		email=data["email"]
		subject=data["subject"]
		message=data["message"]
		csv_write=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_write.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thanku.html')
    else:
        return 'Something is wrong'


# @app.route('/about.html')
# def about():
# 	return render_template('about.html')	

# @app.route('/services.html')
# def services():
# 	return render_template('services.html')

# @app.route('/blog.html')
# def blog():
# 	return render_template('blog.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')	

