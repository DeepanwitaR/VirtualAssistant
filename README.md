# VirtualAssistant
A small project where I created a simple text-based virtual assistant using Gen AI to introduce myself to a user. :) (This is my first ever attempt at GenAI.)

## Background
A **virtual assistant** is a program that lives on the computer say a website or an application, that interacts with a user like a human being through text or audio. We feel like it is a person answering our questions, except it is a fully independent software system that is acting. Let us understand what it is and thus how will we be bringing one to life.

These can take in audio/text as input from the user, then make sense of the sentence with context and relevance and finally produce text/audio to give a meaningful response. 

How is this possible? **Machine learning** - the science of teaching a computer system to mimic human thoughts and responses. This is done through maths and logic, which enables it to process input(by breaking them into small logical pieces of information called vectors), churn out an accepted logical answer (processing through algebra), and learn from each round of calculations(whether an answer was good or not and how can it be made better - error feedback loops). There are many different problems in the world to solve and thus it's helpful to have different approaches to machine learning for each, these are called **machine learning models**. 

Just like humans, there is a need for supervision, i.e. to tell when something is being done right or wrong. In the computing world, this is called **supervised learning**, which these models which we are dealing with here undertake. Therefore, we are now able to see a correlation between a human and a system that acts like a human - how a human learns and how a system that tries to mimic a human learns e.g. when to say what, what is the right answer in this context, etc.

Since we are specifically interested in processing and producing language and sentences, we will be dealing with **Natural Language Processing** models.

This is a gist of what we are working with.

## Using OpenAI
[Open AI](https://openai.com/) is an organization that pioneered the field of creating language processing models which they have trained with thousands of data sets (information which they have found all across the internet) and made available to the public for use. Each of these has its unique features but all of them are capable of using for mimicking human interactions and thus make a great 'brain' for a virtual assistant. Thus I have chosen this provider for my project.

There are numerous tools and models on their site. A very interesting one happens to be [Assitance AI](https://platform.openai.com/docs/assistants/overview) (which is also one of their latest releases currently in its Beta version). This is geared to be a one-stop solution for creating a virtual assistant for your needs - with a set of models and tools to support it. However, since this is a very sophisticated solution that also happens to be charged we look for other alternatives. In practice too this may not be the best tool for a robust solution as it's not heavily tried and tested yet.

Upon searching further I have found a best-suited solution for my project. The [Chat Completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)! With this:
1. I can cater to my basic need of text generation - passing a conversation string and getting back a good response.
2. Not a beta software so it is fairly robust.
3. it is free of charge and easy to use!

Thus my choice for the project prototype.

## Architecture of the core Virtual Assistant Logic
![image](https://github.com/DeepanwitaR/VirtualAssistant/assets/24522364/f61555a3-bf93-474a-94a1-c45391ec9edb)

The above is our architecture diagram. 

The flow in red is the [authentication](https://platform.openai.com/docs/api-reference/authentication) flow where a user must generate their own OpenAI Authentication Key, to access the OpenAI endpoints and in turn the model that sits behind it. This is a prerequisite step and we do it once in the beginning.

The flow in blue is our application flow, where we are hosting a basic Python HTTP server (written with the [Flask Web Framework](https://flask.palletsprojects.com/en/3.0.x/))to take in our user questions as requests and return a response.

Our Python code takes in our **request sentence** and in turn, includes it in the OpenAI client request along with **context information** for every run (we cannot retrain the model but we can make it remember relevant details through context each time) which is the Resume Information present in information.txt and **the NLP model** we want to interact use and interact with in each request and post it to the OpenAI endpoint. _(Note:- information is not retained across sessions and so we must provide it as context at every turn)_

We do this as the remote model on its own is trained to answer questions fairly, but we want it to know and answer with specific information that only we have with us. 

We post the request to the OpenAPI endpoint and return the response from it to the Python server which in turn sends to the user.

## Environment Setup and Executing Virtual Assistant Code Standalone
This section discusses how to set up and run the project in a standalone manner.
1. This is a Python-based implementation (developed with Python 3.10.4), which has been developed over Ubuntu (developed over Ubuntu 22.04 LTS). Run the following to set up Python and its dependencies, and also OpenAI libraries.
```
sudo apt update
sudo apt install python3
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

sudo apt install python3-pip
pip install --upgrade openai
pip install -U Flask
```
2. We then visit the [Open AI API Keys](https://platform.openai.com/api-keys) site to generate our key. (OpenAI_API_Key)
3. To finally run the program we execute the following:
```
git clone https://github.com/DeepanwitaR/VirtualAssistant.git # clone the repository
cd VirtualAssistant # enter the root directory
export OPENAI_API_KEY=<OpenAI_API_Key> # export the Open AI key into the environment
python3 virtualasst.py # run the application
```

## Python server APIs
```
curl localhost:8000/ --header 'Content-Type: text/plain' --data-raw '<your question to the bot>' # user query to application
curl localhost:8000/health # health check API
```
Upon a successful run with sample questions answered the output looks like the following:
For user requests:
![image](https://github.com/DeepanwitaR/VirtualAssistant/assets/24522364/28166419-5779-43d9-ab09-cdd000c163c5)
For health checks to the server:

![image](https://github.com/DeepanwitaR/VirtualAssistant/assets/24522364/c2592c45-2837-45a2-bc5c-7d0c7d323d5e)

## Containerizing and Deploying The Application
In real-time, applications deployed for enterprise-grade use, need to be far more robust in action. We need to create an architecture supporting our core program in such a way that it is always:
1. available to the user or any client program using(**fault tolerant**)
2. can route requests well without overheating the server logic (**load balancing**)
3. easy to deploy and migrate (**small footprint, portability, and platform independence**)
4. easy to change overall application architecture and logic (**decoupled solution**)

The best approach to tackle these is containerizing the application and deploying it as a part of a container ecosystem with an orchestrator.

Imagine you could run almost any application in the world regardless of how different they are (from each other or the host system's OS), on your PC or server. Not only that! you could create a functioning application with them interacting with each other as well and the process takes up fewer resources on the host. That is what containers are! They are essentially any application packaged into lightweight containers (thus the name). Container providers are those involved in developing and maintaining this technology and their products. You can download their software program which is a platform on which containers are designed to run and which is designed to sit over your computer well.

We have chosen [Docker](https://www.docker.com/) as our container provider.

A container will run some logic, and different containers will do different tasks. We now have to meaningfully orchestrate them to create one big, unified, and powerful application. Softwares that do so are called container orchestrators.
Docker also provides an offering called Docker Swarm. However, we will be going with [Kubernetes](https://kubernetes.io/), since:
1. it has many features making our task easier with more capabilities
2. free of cost
3. lots of users thus developer discussion threads for reference
4. my familiarity with it. :)





