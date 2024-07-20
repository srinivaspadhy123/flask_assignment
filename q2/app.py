from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def final_page():
    return "Form submitted successfully"


if __name__ == "__main__":
    app.run("0.0.0.0",port=4040,debug=True)