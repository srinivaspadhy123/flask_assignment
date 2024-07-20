from flask import Flask,render_template,request,redirect,url_for
import os

app = Flask(__name__)
app.config['file_dir'] = 'filesdir'

allowed_file_formats = ('txt','pdf','jpeg','png','jpg','gif')

def validate_file_format(filename):
    return '.' in filename and filename.split('.')[-1] in allowed_file_formats

@app.route("/")
def home_page():
    files = os.listdir(app.config['file_dir'])
    return render_template("index.html",files=files)


@app.route("/upload",methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file and validate_file_format(file.filename):
        file.save(os.path.join(app.config['file_dir'],file.filename))
        # return redirect(url_for("home_page"))
        return file

if __name__ == '__main__':
    if not os.path.exists(app.config['file_dir']):
        os.makedirs('filesdir')
    app.run(host='0.0.0.0',port=4040,debug=True)