from flask import Flask,request,jsonify,flash,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
from user_model import User
import logging as log
log.basicConfig(level= log.INFO)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/postgres'
db = SQLAlchemy(app)
app.secret_key = 'srinivas_padhy'
login_manager = LoginManager(app) 

@app.route('/login',methods=['POST','GET'])
def login():
    username = request.form.get('name')
    password = request.form.get('password')
    user = validate_user(username)
    if user:
        login_user(user)
        log.info("Successfully logged in.")
        # flash("User Logged In Successfully")
        return redirect(url_for('display_user'))

    else:
        return "Invalid Login Credentials."

@app.route("/home")
@login_required
def display_user():
    return f"Hi {current_user.name}, Welcome to the world of Artificial Intelligence!!!"

@app.route("/logout",methods=['DELETE'])
@login_required
def logout():
    logout_user()
    return "User Successfully logged out."

@login_manager.user_loader
def load_user(user_id):
    query = text(f"SELECT * FROM user_table WHERE id='{user_id}'")
    data = db.session.execute(query).fetchone()
    log.info(data)
    if data:
        user = User(data[0],data[1],data[2],data[3])
        return user
    else:
        return None
    
def validate_user(username):
    query = text(f"SELECT * FROM user_table WHERE name='{username}'")
    data = db.session.execute(query).fetchone()
    log.info(data)
    if data:
        user = User(data[0],data[1],data[2],data[3])
        return user
    else:
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4040)