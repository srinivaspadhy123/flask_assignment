from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from model import DbModel
from sqlalchemy import text
import logging as log
log.basicConfig(level= log.INFO)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1/postgres'
db = SQLAlchemy(app)
db_model = DbModel()

@app.route("/users",methods=['GET'])
def get_users():
    query = text("SELECT id, name, city, state FROM user_table")
    result = db.session.execute(query)
    users = [DbModel(row.id,row.name,row.city,row.state) for row in result]
    user_list = [{'id':user.get_id(),'name':user.get_name(),'city':user.get_city(),'state':user.get_state()}for user in users]
    db.session.commit()
    db.session.close()
    return jsonify(user_list)

@app.route("/add_user",methods=['POST'])
def add_user():
    data = request.get_json()
    db_model.set_id(data['id'])
    db_model.set_city(data['city'])
    db_model.set_name(data['name'])
    db_model.set_state(data['state'])
    query = text(f"INSERT INTO user_table(id,name,city,state) VALUES('{db_model.get_id()}','{db_model.get_name()}','{db_model.get_city()}','{db_model.get_state()}')")
    db.session.execute(query)
    db.session.commit()
    db.session.close()
    return "User Data Successfully added."

@app.route("/update_user/<string:user_id>",methods=['PATCH'])
def update_user(user_id):
    name = request.args.get('name')
    request_data = request.get_json()
    city = request_data['city']
    state = request_data['state']
    fetch_query = text(f"SELECT id, name, city, state FROM user_table WHERE id='{user_id}' AND name='{name}'")
    data = db.session.execute(fetch_query)
    result = data.fetchone()
    if result:
        db_model.set_id(user_id)
        db_model.set_name(name)
        db_model.set_city(city)
        db_model.set_state(state)
    update_query = text(f"UPDATE user_table SET city='{db_model.get_city()}',state='{db_model.get_state()}' WHERE id='{user_id}' AND name='{name}'")        
    db.session.execute(update_query)
    db.session.commit()
    db.session.close()

    return "Record Successfully Updated."


@app.route("/delete_user/<string:user_id>",methods = ['DELETE'])
def delete_user(user_id):
    delete_query = text(f"DELETE FROM user_table WHERE id='{user_id}'")
    db.session.execute(delete_query)
    db.session.commit()
    db.session.close()
    return "user successfully deleted"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4040)
