from flask import *
from flask_restful import Resource


app = Flask(__name__)

app.add_resource('sum/<a>/<b>', endpoint='sum')


def get_sum(a,b):
	return jsonify(str(int(a)+int(b)))
   		
@app.route(sum, methods=['GET'])

if __name__ == '__main__':
	app.run(debug=True)
