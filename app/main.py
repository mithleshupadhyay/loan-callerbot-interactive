from flask import Flask, request, jsonify

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.chatbot import start_chatbot
from app.call_handler import initiate_call
from app.database import setup_pinecone

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start():
    # Call Pinecone setup and chatbot start
    setup_pinecone()
    user_data = request.json
    return start_chatbot(user_data)

@app.route('/start_call', methods=['POST'])
def start_call():
    # This will trigger the call using Twilio when user submits their contact details
    user_data = request.json
    initiate_call(user_data)
    return {'status': 'Call started successfully'}

from twilio.twiml.voice_response import VoiceResponse

@app.route('/voice', methods=['GET', 'POST'])
def voice():
    response = VoiceResponse()
    response.say("Hi, I'm calling from the AI loan assistant system. Can I ask you a few questions to help you with your home loan?")
    response.gather(num_digits=1, action="/handle-key")
    return str(response)

@app.route('/handle-key', methods=['GET', 'POST'])
def handle_key():
    response = VoiceResponse()
    response.say("Thanks for your response. We will proceed with your request.")
    return str(response)


if __name__ == '__main__':
    app.run(port=5000)
    app.run(debug=True)
