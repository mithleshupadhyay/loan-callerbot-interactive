import openai
import pinecone

from dotenv import load_dotenv
load_dotenv()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import get_product_info_from_pinecone

# Load OpenAI API key from environment variables

openai.api_key = os.getenv("OPENAI_API_KEY")

def start_chatbot(user_data):
    name = user_data.get("name")
    phone_number = user_data.get("phone_number")
    
    # Greeting the user
    greeting_message = f"Hi {name}, I'm your AI loan assistant! How can I help you with your loan needs today?"
    
    # Start the conversation
    conversation = {
        'user_message': greeting_message,
        'product_info': get_product_info_from_pinecone(),
    }
    
    # Use OpenAI's GPT for follow-up questions and answers
    answer = generate_response(greeting_message)
    return {'response': answer}

def generate_response(greeting_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use a chat model like gpt-3.5-turbo
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": greeting_message}],
        max_tokens=150
    )
    # Extract and return the response text
    return response['choices'][0]['message']['content']

