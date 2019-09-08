""" Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. """


from webexteamssdk import WebexTeamsAPI
from flask import Flask, request
from cards import input_card
from sys import stdout


app = Flask(__name__)

def get_attachments(self, id):
    '''
    Bound method added to the WebexTeamsAPI to get attachments for a new feature called Adaptive Cards
    '''
    json_data = self._session.get('/attachment/actions/' + id)
    return json_data

@app.route('/', methods=['POST'])
def index():
    if request:

        wbxapi = WebexTeamsAPI()
        # Bind a method to the WebexTeamsAPI class
        WebexTeamsAPI.get_attachments = get_attachments

        request_json = request.get_json()
        print(type(request))
        print(request.args.get('data'))
        print(type(request_json))
        print(request_json)
        stdout.flush()

        if request.args and 'data' in request.args:
            webhook = request.args.get('data')
            room_id = webhook['roomId']
            wbxapi.messages.create(roomId=room_id, text='Oops! Something is broken or you are using the mobile app for which cards are not supported yet.', attachments=input_card)

        elif request_json and 'data' in request_json:
            room_id = webhook['data']['roomId']
            wbxapi.messages.create(roomId=room_id, text='Oops! Something is broken or you are using the mobile app for which cards are not supported yet.', attachments=input_card)

        else:
            return f'Hello World!'
