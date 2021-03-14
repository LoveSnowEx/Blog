import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()


class User(db.Document):
    confirmed_at = db.DateTimeField(default=datetime.datetime.now,
                                    required=True)
    email = db.StringField(max_length=255, unique=True)
    username = db.StringField(max_length=255)
    password = db.StringField(max_length=255)

    @classmethod
    def loginVerify(cls, email, password):
        user = User.objects(email=email).first()
        if user:
            if user.password == password:
                return 0
            else:
                return 1
        else:
            return 2

    @classmethod
    def register(cls, email, password):
        username = email.split('@')[0]
        user = User(email=email, username=username, password=password)
        user.save()


class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    author = db.ReferenceField(User, required=True)
    title = db.StringField(min_length=1, max_length=30, required=True)
    content = db.StringField()
    tags = db.ListField(db.StringField(max_length=30))
    meta = {
        'indexes': ['-created_at', 'tags', 'title', 'author'],
        'ordering': ['-created_at', 'tags'],
    }
