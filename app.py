from flask import Flask, jsonify , request
from werkzeug.exceptions import BadRequest
from flask_cors import CORS
import smtplib
# from namegen import Dragon_name



app = Flask(__name__)
CORS(app)

all_dragon =[
    {'id': 1, 
    'name': 'Drogon'},
    {'id': 2,
    'name': 'Viserion'},
    {'id': 3,
    'name': 'Rhaegal'}
]


@app.route('/', methods = ['GET'])
def home():
    return 'Welcome to dragon and penguin name'

@app.route('/dragonname', methods = ['GET', 'POST'])
def dragon_name():
    if request.method == 'GET':
        return jsonify(all_dragon)
    if request.method == 'POST':
        new_dragon = request.get_json()
        all_dragon.append(new_dragon)
        new_dragon['id'] = len(all_dragon)
        return jsonify({'dragon': new_dragon})

@app.route('/dragonname/<int:id>', methods = ['GET'])
def dragon(id):
    if request.method == 'GET':
        dragon = all_dragon[id -1]
        return jsonify(dragon)
    # if request.method == 'DELETE':
    #     dragon_id = dragon(id-1)
    #     all_dragon.remove(dragon)
    #     return dragon, 204
       
@app.route('/penguinname', methods = ['GET'])
def penguin_name():
    if request.method == 'GET':
        return jsonify(message= 'Hi')

def test_api_penguinname(client):
    res = client.get(url_for('api.penguinname'))
    assert res.json == {'message': 'Hi'}

def test_app(client):
    assert client.get(url_for('api.penguinname')).status_code == 200
# if __name__ == "__main__":
#     test_api_penguinname(client)
#     test_api_penguinname_tuple()
#     print("Everything passed")

# def find_by_id(id):
#     try:
#         return next(dragon for dragon in all_dragons if dragon['id'] == id)
#     except:
#         raise BadRequest(f"we don't have that dragon {id}!")




app.run(debug = True)