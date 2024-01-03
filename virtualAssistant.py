# basic virtual asst program 

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Deepa is from Singapore and works at Dell."},
    {"role": "user", "content": "Where is Deepa from?"},
    {"role": "user", "content": "What does Deepa do?"},
    # {"role": "user", "content": "She is Deepa"},
    {"role": "assistant", "content": "I know Deepa."},
    # {"role": "user", "content": "Where was it played?"}
  ]
)

response_message = response.choices[0].message.content
print(response_message )
