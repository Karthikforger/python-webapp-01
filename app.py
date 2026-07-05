from flask import Flask,render_template,url_for,request,redirect  

app= Flask(__name__)

@app.route('/')
def home():
    # return render_template('base.html')
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign')
def sign_up():
    return render_template('signup.html')
