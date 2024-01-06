import requests

url="http://localhost:30001/"

while 1:
    healthCheckResponse = requests.get(url + "health")
    if healthCheckResponse.status_code == 200:
        print('Server Ready!')
        break
    else:
        print('Waiting for server to be ready...')

print('Welcome! I am a virtual assistant to tell you about Deepa. Please ask your questions!')

headers = {
    'Content-Type': 'text/plain',
}

# # format the string coming on as a response
def formattingFunc(byteString):
    string = byteString.decode("utf-8")
    string = string.rstrip("\n'")
    return string

while 1:
    question = input('\n')
    virtAsstResponse = requests.post(url, headers = headers, data = question)
    if virtAsstResponse.status_code== 200:
        print(formattingFunc(virtAsstResponse.content))
    else:
        print('Server error processing query.')
