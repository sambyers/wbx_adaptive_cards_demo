from webexteamssdk import WebexTeamsAPI
from flask import Flask, request
from cards import input_card


app = Flask(__name__)

def get_attachments(self, id):
    '''
    Bound method added to the WebexTeamsAPI to get attachments for a new feature called Adaptive Cards
    '''
    json_data = self._session.get('/attachment/actions/' + id)
    return json_data

@app.route('/', methods=['GET'])
def index():
    if request:

        wbxapi = WebexTeamsAPI()
        # Bind a method to the WebexTeamsAPI class
        WebexTeamsAPI.get_attachments = get_attachments

        request_json = request.get_json()

        if request.args and 'body' in request.args:
            webhook = request.args.get('body')
            room_id = webhook['data']['roomId']
            wbxapi.messages.create(roomId=room_id, text='Oops! Something is broken or you are using the mobile app for which cards are not supported yet.', attachments=input_card)

        elif request_json and 'body' in request_json:
            webhook =  request_json['body']
            room_id = webhook['data']['roomId']
            wbxapi.messages.create(roomId=room_id, text='Oops! Something is broken or you are using the mobile app for which cards are not supported yet.', attachments=input_card)

        else:
            return f'Hello World!'
