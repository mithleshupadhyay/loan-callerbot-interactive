from twilio.rest import Client
import os

from dotenv import load_dotenv
load_dotenv()

# Set up Twilio client
twilio_client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

def initiate_call(user_data):
    phone_number = user_data.get("phone_number")
    
    # Generate greeting message and start the call
    greeting_message = f"Hi, I'm calling from the AI loan assistant system. Can I ask you a few questions to help you with your home loan?"

    call = twilio_client.calls.create(
        to=phone_number,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        url='https://2b2b-2409-40c4-28a-d3cf-c9b4-34b1-e116-db5c.ngrok-free.app/voice',  # Use ngrok URL for voice interaction
    )
    return call.sid
