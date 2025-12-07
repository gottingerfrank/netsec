import requests
import os
import openai

openai_api_key = os.getenv('OPENAI_API_KEY')
prompt = 'What are the steps of the MITRE Cyber Kill Chain?'

client = openai.OpenAI()
response = client.chat.completions.create(model="gpt-3.5-turbo-instruct", prompt=prompt)

res_choice = response.choices[0].message.content.strip()

# client = openai.completions.create(model="gpt-3.5-turbo-instruct" , prompt)


print(res_choice)
