import os

from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{'role': 'system',
                                                                            'content': 'Explain the MITRE Cyber Kill Chain'
                                                                            }])

for r in response.choices:
    print(r.message.content.strip())
