from flask import *
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#@api.route(sum, methods=['GET'])

class SumAPI(Resource):
	def get(self,a,b):
		return int(a)+int(b)
		
class SubAPI(Resource):
	def get(self,a,b):
		return int(a)-int(b)
		
class DivAPI(Resource):
	def get(self,a,b):
		return int(a)/int(b)

class MultAPI(Resource):
	def get(self,a,b):
		return int(a)*int(b)


api.add_resource(SumAPI,'/sum/<a>/<b>', endpoint='sum')
api.add_resource(SubAPI,'/sub/<a>/<b>', endpoint='sub')
api.add_resource(DivAPI,'/div/<a>/<b>', endpoint='div')
api.add_resource(MultAPI,'/mult/<a>/<b>', endpoint='mult')



if __name__ == '__main__':
	app.run(debug=True)
