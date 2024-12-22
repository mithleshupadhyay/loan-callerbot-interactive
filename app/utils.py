import json
from app.database import get_product_info_from_pinecone

def save_conversation_to_db(user_data):
    # Save conversation to database or local storage
    # Here we are just printing, in real case save to DB
    with open("conversation_log.json", "a") as file:
        file.write(json.dumps(user_data) + "\n")
    return "Conversation saved!"

def parse_product_query(query):
    # You can use the query to fetch matching products
    return get_product_info_from_pinecone()
