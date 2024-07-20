from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = 'srinivas'
@app.route("/")
def user_form():
    return render_template("index.html")

@app.route("/login",methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    session['username'] = username
    # return render_template('user_data.html')
    return redirect('/submit')

@app.route("/submit",methods=['POST','GET'])
def user_data():
    
    username = session['username']
    if request.method=='POST':
        city = request.form.get('city')
        state = request.form.get('state')
        
        return f"{username},{state},{city}"
    return render_template('/user_data.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4040,debug=True)