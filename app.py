from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [
    {
        "id":0,
        "title":"sun of rise",
    },
     {
        "id":1,
        "title":"game of throns",
    },
]

@app.route('/books',methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if len(book_list)>0:
            return jsonify(book_list)
        else:
            'Nothing Found', 404

    if request.method == 'POST':    
        new_title = request.form['title']
        iD = book_list[-1]['id']+1

        new_obj = {
            'id':iD,
            'title':new_title
        }
        book_list.append(new_obj)
        return jsonify(book_list), 201

if __name__ == '__main__':
    app.run(debug=True)