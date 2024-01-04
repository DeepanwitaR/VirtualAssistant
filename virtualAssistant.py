# Virtual Assistant program
from openai import OpenAI

client = OpenAI()

def readFileFunc():
  textFile = open("./information.txt", "r")
  textData = textFile.read()
  textFile.close()

  return textData


# Function to send questions to the ML model powered by Open API.
def textGenerationAPIFunc(question):
  textData = readFileFunc()
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": textData}, # we have to provide context for every round of ML query (as a pretraining) since model does not retain information across session.
      {"role": "user", "content": question},
    ]
  )
  response_message = response.choices[0].message.content
  print(response_message )


print('Welcome! I am an OpenAI based virtual assistant. How may I assist you?')
while 1:
    question = input('\n')
    textGenerationAPIFunc(question)
