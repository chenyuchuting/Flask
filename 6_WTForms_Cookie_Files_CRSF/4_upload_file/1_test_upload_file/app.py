from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from forms import UpLoadForm
from werkzeug.datastructures import CombinedMultiDict
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
        # flask.request.files和flask.request.form来进行合并再传到form中进行验证
        form = UpLoadForm(CombinedMultiDict([request.form, request.files]))  # request.form类似元组类型
        if form.validate():
            # desc = request.form.get("desc")
            # file = request.files.get("avatar")
            desc = form.desc.data
            file = form.avatar.data
            # 此函数获取文件名时安全，但对中文名获取时，获取不到中文
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_PATH, filename))
            print(desc)
            return "文件上传成功！"
        else:
            print(form.errors)
            return "Fail"


@app.route('/images/<filename>/')
def get_image(filename):
    # url:http://127.0.0.1:5000/images/avatar.jpeg/
    return send_from_directory(UPLOAD_PATH, filename)


if __name__ == '__main__':
    app.run()
