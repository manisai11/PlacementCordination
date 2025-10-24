"""from flask import Blueprint, request, jsonify
# New import for the unified SDK is 'google.genai'
from google import genai
from .config import GEMINI_API_KEY
from google.genai.errors import APIError 

chatbot_bp = Blueprint("chatbot_bp", __name__)

# 1. INITIALIZE THE CLIENT
# The client object is initialized once and handles all model calls.
# It uses the API key for authentication.
try:
    client = genai.Client(api_key=GEMINI_API_KEY)
    MODEL_NAME = "gemini-1.5-flash"
except Exception as e:
    # Handle the case where the key is invalid or missing
    print(f"Error initializing GenAI Client: {e}")
    # You might want to shut down or return an error here instead of proceeding
    client = None

@chatbot_bp.route("/chat", methods=["POST"])
def chat_with_gemini():
    if not client:
        return jsonify({"error": "AI service is not configured correctly."}), 503

    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400
    
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        # 2. USE 'generate_content' ON THE CLIENT OBJECT
        # The prompt is now passed as the 'contents' argument.
        prompt = f"You are a helpful placement assistant. Answer student queries clearly.\n\nUser: {user_message}\nAI:"
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt 
        )
        
        # 3. ACCESS THE REPLY using '.text'
        ai_reply = response.text

        return jsonify({"reply": ai_reply})
    
    except APIError as e:
        # Handle specific API errors (e.g., bad request, rate limit)
        print("Gemini API error:", e)
        return jsonify({"error": f"AI API Error: {str(e)}"}), 500
    except Exception as e:
        # Handle other unexpected errors
        print("General error:", e)
        return jsonify({"error": str(e)}), 500"""

import os
from google import genai
from flask import Blueprint, request, jsonify
# New import for the unified SDK is 'google.genai'
from google import genai
from .config import GEMINI_API_KEY
from google.genai.errors import APIError 

chatbot_bp = Blueprint("chatbot_bp", __name__)
# 1. Install the SDK: pip install google-genai

try:
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception as e:
    pass
# 3. Define the model and content
MODEL_NAME = "gemini-2.5-flash" 

@chatbot_bp.route("/chat", methods=["POST"])
def chat_with_gemini():
    if not client:
        return jsonify({"error": "AI service is not configured correctly."}), 503

    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400
    
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "Message is required"}), 400


    # 4. Make the API call
    try:
        prompt = f"You are a helpful placement assistant. Answer student queries clearly.\n\nUser: {user_message}\nAI:"

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"An error occurred during the API call: {e}")