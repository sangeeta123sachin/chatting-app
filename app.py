# from flask import Flask,jsonify,request
# app=Flask(__name__)
# users=[
#      {
#      'id':2,
#      'name':'Manas',
#      'age':20
#      },
#      {
#      'id':1,
#      'name':'Vaishali',
#      'age':19
#      },
#      {
#      'id':3,
#      'name':'Vipin',
#      'age':21
#      }
# ]
# @app.route('/')
# def index():
# 	return app.send_static_file('index.htm')
	
# @app.route('/users')
# def get_users():
# 	return jsonify(users)
# @app.route('/users/<id>')
# def get_user(id):
# 	user=list(filter(lambda u:str(u['id'])==id,users))
# 	return jsonify(user)





# if __name__=="__main__":
# 	app.run()
from flask import Flask,jsonify,request
from flask_socketio import SocketIO

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users=[
     {
     'id':2,
     'name':'Manas',
     'age':20
     },
     {
     'id':1,
     'name':'Vaishali',
     'age':19
     },
     {
     'id':3,
     'name':'Vipin',
     'age':21
     }
]
@app.route('/')
def index():
     return app.send_static_file('index.html')
     
@app.route('/users')
def get_users():
     return jsonify(users)

@app.route('/users/<id>')
def get_user(id):
     user=list(filter(lambda u:str(u['id'])==id,users))
     return jsonify(user)
     
@socketio.on('message')
def handle_message(data):
     socketio.emit('push',data,broadcast=True,include_self=False)
if __name__=="__main__":
     socketio.run(app)











































































