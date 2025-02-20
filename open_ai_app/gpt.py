from password import MY_OPEN_AI_API_KEY
import openai

openai.api_key = MY_OPEN_AI_API_KEY

class GPT:
    def __init__(self):
        self.chat_model = "gpt-4o-mini"
        self.image_model = "dall-e-3"

    def chat(self, user_message):
        response = openai.ChatCompletion.create(
            model=self.chat_model,
            messages=[{"role": "user", "content": user_message}]
        )
        return response["choices"][0]["message"]["content"]

    def image(self, user_message):
        response = openai.Image.create(
            model=self.image_model,
            prompt=user_message
        )
        return response["data"][0]["url"]
