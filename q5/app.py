from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key = "srinivaspadhy"

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/login",methods = ['POST'])
def user_login():
    username = request.form.get('username')
    session['username'] = username
    return redirect("/display_info")

@app.route("/display_info")
def display():
    return f"logged in username is {session['username']}"




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4040,debug=True)