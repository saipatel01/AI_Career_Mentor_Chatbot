import os
from google import genai
from config.settings import GEMINI_API_KEY
import logging

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def create_chat(self, system_prompt):
        try:
            chat_session = self.client.chats.create(
                model="gemini-2.5-flash",
                config=genai.types.GenerateContentConfig(
                    system_instruction=system_prompt
                )
            )
            return chat_session
        except Exception as e:
            logging.error(f"Chat creation error: {e}")
            raise

    def send_message(self, chat_session, message):
        try:
            response = chat_session.send_message(message)
            return response.text
        except Exception as e:
            logging.error(f"Send message error: {e}")
            return "⚠️ Sorry, I am facing technical issues."