import os
from typing import List, Dict
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError
from groq import Groq
from flask_cors import CORS

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("API key for Groq is missing. Please set the GROQ_API_KEY in the .env file.")

app = Flask(__name__)
CORS(app)  # Enable CORS

client = Groq(api_key=GROQ_API_KEY)

# In-memory conversation storage
conversations: Dict[str, Dict] = {}

class UserInput(BaseModel):
    message: str
    role: str = "user"
    conversation_id: str

class Conversation:
    def __init__(self):
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": "You are a useful AI assistant."}
        ]
        self.active: bool = True

def query_groq_api(conversation: Conversation) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation.messages,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        return response

    except Exception as e:
        raise Exception(f"Error with Groq API: {str(e)}")

def get_or_create_conversation(conversation_id: str) -> Conversation:
    if conversation_id not in conversations:
        conversations[conversation_id] = Conversation()
    return conversations[conversation_id]

@app.route("/chat/", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        try:
            user_input = UserInput(**data)
        except ValidationError as e:
            return jsonify({"error": e.errors()}), 400

        conversation = get_or_create_conversation(user_input.conversation_id)

        if not conversation.active:
            return jsonify({"error": "The chat session has ended. Please start a new session."}), 400

        # Append user message
        conversation.messages.append({
            "role": user_input.role,
            "content": user_input.message
        })

        # Query Groq API
        response = query_groq_api(conversation)

        # Append assistant response
        conversation.messages.append({
            "role": "assistant",
            "content": response
        })

        return jsonify({
            "response": response,
            "conversation_id": user_input.conversation_id
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
