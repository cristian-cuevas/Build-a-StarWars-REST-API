"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)


@app.route('/users')
def listUser():
    all_users = User.query.all()
    all_users = list(map(lambda user: user.serialize(), all_users))
    return jsonify(all_users)

@app.route('/user', methods = ['POST'])
def add():
    data = request.get_json()
    print (data)
    if data['id'] is None or data['email'] is None:
        return 'Empty params'
    if 'password' not in data:
        return 'Empty password'
    user = User()
    user.id = data['id']
    user.email = data['email']
    user.is_active = True
    user.password = data['password']
    db.session.add(user)
    db.session.commit()
    print (user.__repr__())
    return user.serialize()

@app.route('/user/<int:userId>', methods = ['DELETE'])
def delete(userId):
    user = User.query.get(userId)
    if user is None:
        return "User doesn't exist", 204
    db.session.delete(user)
    db.session.commit()
    return "Deleted", 200

@app.route('/user/<int:id>')
def get(id):
    user = User.query.get(id)
    if user is None:
        return {}
    return user.serialize()