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
    return render_template('login.html')

@app.route('/sign', methods=["GET","POST"])
def sign_up():
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        return render_template('welcome.html', name=name, email=email, password=password)
    return render_template('signup.html')
# @app.route('home')
# def home
# @app.route('/about')
# def about():
#     return render_template('home.html')

# @app.route('/contact_us')
# def contact_us():
#     return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('Login.html')

# @app.route('/sign_up')
# def sign_up():
#     return render_template('home.html')

# @app.route('/', methods=["GET","POST"])
# def login():
#     # if request.method== "POST":
#     #     return redirect(url_for(home))
#     return render_template("Login.html")

# @app.route('/home', methods=["GET","POST"])
# def home():
#     if request.method == "POST":
#         name=request.form.get("name")
#         email=request.form.get("email")
#         password=request.form.get("password")
#         return render_template("welcome.html", list=[name,email,password])
#     return render_template("home.html")

# @app.route('/about')
# def about():
#     return "you are on the about page"

# @app.route("/testing", methods=["GET","POST"])
# def testing():
#     if request.method=="GET":
#         return "you are viewing"
#     else :
#         return "you just typed"
