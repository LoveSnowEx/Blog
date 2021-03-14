from flask import Flask, render_template, request, url_for, redirect, session
from config import DevConfig
from models import db, User, Post

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)


def get_posts():
    return Post.objects()


def get_post(hash_code):
    return Post.objects().first()


def signin(id):
    session['id'] = id


@app.route('/editor/', methods=['GET'])
def editor():
    return render_template('editor.html', post=get_post())


@app.route('/editor/', methods=['POST'])
def save_post():
    # print(post.title)
    # if post.validate():
    # 	post.save()
    # 	print('save success')
    return redirect(url_for('viewer', hash_code=0))


@app.route('/viewer/<string:hash_code>')
def viewer(hash_code):
    return render_template('viewer.html', post=get_post(hash_code))


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    verify_code = User.loginVerify(email, password)

    if verify_code == 0:
        login(email)
        return redirect(url_for('index'))
    if verify_code == 1:
        return redirect(url_for('index'))
    if verify_code == 2:
        User.register(email, password)
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')


def main():
    app.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
