from services.gemini_service import GeminiService
from prompts.system_prompt import SYSTEM_PROMPT

class ChatController:

    def __init__(self):
        self.gemini = GeminiService()
        self.chat_session = self.gemini.create_chat(SYSTEM_PROMPT)

    def get_response(self, user_input):
        return self.gemini.send_message(self.chat_session, user_input)