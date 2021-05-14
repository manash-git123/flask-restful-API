import pymongo
from pymongo import MongoClient
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/')
def landing():
    return {"note": "This URL is not supposed to be hit"}

@app.route('/set_user', methods=['POST'])
def set_user():
    cluster = MongoClient("mongodb+srv://applicationUsers:manashmanash@cluster0.cd6ca.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster.Users
    collection = db.user_details

    raw_data = request.get_json()

    _id = collection.count()
    _name = raw_data['name']
    _email = raw_data['email']
    _district = raw_data['district']
    _state = raw_data['state']

    post = {
        "_id": _id,
        "name": _name,
        "email": _email,
        "district": _district,
        "state": _state
    }
    collection.insert_one(post)

    return post


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)   
