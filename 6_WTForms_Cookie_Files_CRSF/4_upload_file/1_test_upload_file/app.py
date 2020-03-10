from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        desc = request.form.get("desc")
        file = request.files.get("avatar")
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_PATH, filename))
        print(desc)
        return "文件上传成功！"


@app.route('/images/<filename>/')
def get_image(filename):
    # url:http://127.0.0.1:5000/images/avatar.jpeg/
    return send_from_directory(UPLOAD_PATH, filename)


if __name__ == '__main__':
    app.run()
