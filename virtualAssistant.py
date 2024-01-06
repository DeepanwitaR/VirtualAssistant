# Virtual Assistant program
import os
import virtualasst
import openai
from flask import Flask, request

app = Flask(__name__) # create a flask app server instance that will host our application

openAiApiKey = os.getenv('OPENAI_API_KEY')
if openAiApiKey == "":
   print('Missing OPENAI_API_KEY')
   exit()

openai.api_key = openAiApiKey
client = openai.OpenAI()

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
      {"role": "system", "content": textData}, # we have to provide context for every round of ML query (as a pretraining) since the model does not retain information across sessions.
      {"role": "user", "content": question},
    ]
  )
  response_message = response.choices[0].message.content
  return response_message

print('Powering up OpenAI based virtual assistant server...')
# API to serve user requests
@app.route("/", methods = ['GET','POST'])
def getUserQuery():
    virtualAsstQuestion = request.data
    virtualAsstResponse = textGenerationAPIFunc(virtualAsstQuestion.decode("utf-8"))
    return virtualAsstResponse, 200

# health check API
@app.route("/health", methods = ['GET'])
def healthCheck():
    return "Server up and running!", 200

if __name__=="__main__":
  app.run(debug=True,host="0.0.0.0", port=8000) 
  # We are hosting at address 0.0.0.0 so that any IP can resolve it. This is a trick to access the application from outside the pod (which is running on a CNI and would not be accessible otherwise)
