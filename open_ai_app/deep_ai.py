import requests
from password import MY_DEEP_AI_API_KEY

class DeepAI:
    def __init__(self):
        self.api_key = MY_DEEP_AI_API_KEY
        self.img_endpoint = "https://api.deepai.org/api/text2img"
        self.headers = {
            'api-key': self.api_key,
        }

    def get_image(self, text):

        data = {
            'text': text,
        }
        response = requests.post(self.img_endpoint, headers=self.headers, data=data)
        return response.json()





deep_ai = DeepAI()

print(deep_ai.get_image("A beautiful sunset over the mountains."))