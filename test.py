


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
