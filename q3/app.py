from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def start_page():
    return "This is the starting page"

@app.route('/home')
def home_page():
    arg = request.args.get('name')
    arg2 = request.args.get('address')
    return f"{arg} lives in {arg2}"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4040,debug=True)