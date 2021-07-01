from flask import Flask, jsonify, request
import json

app=Flask(__name__)

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

@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def developer(id):
    if request.method =='GET':
        try:
            response = devs[id]
        except IndexError:
            message = 'Inexistent Developer ID {}'.format(id)
            response = {'status':'Error!!!', 'message':message}
        except Exception:
            message = {'Error Unknonw!'}
            response = {'status': 'Error!!!','message': message}
        return jsonify(response)
    elif request.method == 'PUT':
        Data = json.loads(request.data)
        devs[id] = Data
        return jsonify(Data)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'Success! record removed!'})

@app.route('/dev/', methods = ['POST','GET'])
def list_devs():
    if request.method == 'POST':
        Data = json.loads(request.data)
        pos = len(devs)
        Data['id'] = pos
        devs.append(Data)
        return jsonify(devs[pos])#'status': 'success!', 'message':'Inserted record~'})
    else:
        response = devs
        return jsonify(response)
    
if __name__ == '__main__':
    app.run(debug=True)