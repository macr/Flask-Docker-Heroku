from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Greetings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    greeting = db.Column(db.String(256))


@app.route('/')
def hello_world():
    if Greetings.query.count() == 0:
        greeting = Greetings(greeting='Hello, World!')
        db.session.add(greeting)
        db.session.commit()
    print(Greetings.query.all())
    greetings = [f'<p>{i.greeting}</p>' for i in Greetings.query.all()]
    greetings = ' '.join(greetings)
    return greetings
