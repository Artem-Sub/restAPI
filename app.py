from flask import *

app = Flask(__name__)


@app.route('/sum/<a>/<b>', methods=['GET'])
def get_tasks(a,b):
    return jsonify(str(int(a)+int(b)))
	

@app.route('/mult/<a>/<b>', methods=['GET'])
def get_tasks(a,b):
	return str(int(a)*int(b))


@app.route('/div/<a>/<b>', methods=['GET'])
def get_tasks(a,b):
	return str(int(a)/int(b))

@app.route('/sub/<a>/<b>', methods=['GET'])
def get_tasks(a,b):
	return str(int(a)-int(b))


	
if __name__ == '__main__':
    app.run(debug=True)