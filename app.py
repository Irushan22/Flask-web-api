from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

book_list = [
    {
        "updates": [
            {
                "recNo": 1,
                "time": 0,
                "forefoot_strike": 234,
                "midfoot_strike": 2,
                "rarefoot_strike": 2
            },
            {
                "recNo": 2,
                "time": 2,
                "forefoot_strike": 322,
                "midfoot_strike": 2,
                "rarefoot_strike": 2
            }
        ],
        "sensorName": "Smart_shoe_left"
    },
    {
        "updates": [
            {
                "recNo": 1,
                "time": 0,
                "forefoot_strike": 800,
                "midfoot_strike": 2,
                "rarefoot_strike": 2
            },
            {
                "recNo": 2,
                "time": 2,
                "forefoot_strike": 900,
                "midfoot_strike": 2,
                "rarefoot_strike": 2
            }
        ],
        "sensorName": "Smart_shoe_left"
    },
]


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(book_list) > 0:
            response = flask.jsonify(book_list)
            response.headers.add('Access-Control-Allow-Origin', '*')
        else:
            'Nothing Found', 404

    if request.method == 'POST':
        new_title = request.form['title']
        iD = book_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'title': new_title
        }
        book_list.append(new_obj)
        return jsonify(book_list), 201


if __name__ == '__main__':
    app.run(debug=True)
