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

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        return render_template('welcome.html', name=name, email=email, password=password)
    return render_template('login.html')

@app.route('/sign', methods=["GET","POST"])
def sign_up():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        return render_template('welcome.html', name=name, email=email, password=password)
    return render_template('signup.html')
