from app import db, login_manager
from flask_login import UserMixin


# Декоратор @login_manager.user_loader используется для регистрации функции,
# которая загружает пользователя по его идентификатору.
# Эта функция должна принимать идентификатор пользователя и возвращать объект пользователя.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    clicks = db.Column(db.Integer, default=0)


    def __repr__(self):
        return f'User {self.username} - clicks^ {self.clicks}'


