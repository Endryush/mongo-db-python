from flask import Flask, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_all_users():
    users = list(mongo.db.users.find()) 
    users = [{**user, '_id': str(user['_id'])} for user in users]

    return jsonify(users), 200


if __name__ == '__main__':
    app.run(debug=True)