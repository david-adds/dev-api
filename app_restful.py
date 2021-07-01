from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills
import json


app = Flask(__name__)
api = Api(app)

devs=[
        {   
            "id":0,
            "nome": "Jackie",
            "skills":["Python", "Flask"]
        },
        {
            "id":1,
            "nome": "Alison",
            "skills":["Python", "Flask"]
        }
      ]

class Developer(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            message = 'Inexistent Developer ID {}'.format(id)
            response = {'status':'Error!!!', 'message':message}
        except Exception:
            message = {'Error Unknonw!'}
            response = {'status': 'Error!!!','message': message}
        return response
    
    def put(self, id):
        Data = json.loads(request.data)
        devs[id] = Data
        return Data
    
    def delete(self, id):
        devs.pop(id)  
        return {'status': 'Success! record removed!'}    
 
 
 # List all developers and also allow register a new one(s).   
class ListDevs(Resource):
    def get(self):
        response=devs
        return response
    
    def post(self):
        Data = json.loads(request.data)
        position = len(devs)
        Data['id'] = position
        devs.append(Data)
        return devs[position]
        
        
api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(ListDevs, '/dev/')
api.add_resource(Skills, '/skills/')
if __name__ == '__main__':
    app.run(debug=True)