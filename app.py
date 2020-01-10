from flask import Flask, request, jsonify
from dbconn import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/countries')
def get_all_countries():
    """this api gets all the countries in a single array"""
    postgreSQL_select_Query = "select * from countries"

    cursor.execute(postgreSQL_select_Query)
    country_records = cursor.fetchall()

    for row in country_records:
        return jsonify({"country" : row[0], "name": row[1], "states":row[2]})

if __name__ == '__main__':
    app.run(debug=True)
