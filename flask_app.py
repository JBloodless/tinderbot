
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
from settings import token, confirmation_token
import messageHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'

def curr_user_id():
    data = json.loads(request.data)
    user_id = data['object']['user_id']
    return user_id
