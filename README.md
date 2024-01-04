# VirtualAssistant
A small project where I created a simple text-based virtual assistant using Gen AI to introduce myself to a user. :)

## Background
A **virtual assistant** is a program that lives on the computer say a website or an application, that interacts with a user like a human being through text or audio. We feel like it is a person answering our questions, except it is a fully independent software system that is acting. Let us understand what it is and thus how will we be bringing one to life.

These can take in audio/text as input from the user, then make sense of the sentence with context and relevance and finally produce text/audio to give a meaningful response. How is this possible? **Machine learning** - the science of teaching a computer system to mimic human thoughts and responses. This is done through maths and logic, which enables it to process input(by breaking them into small logical pieces of information called vectors), churn out an accepted logical answer (processing through algebra), and learn from each round of calculations(whether an answer was good or not and how can it be made better - error feedback loops). There are many different problems in the world to solve and thus it's helpful to have different approaches to machine learning for each, these are called **machine learning models**. 

Just like humans, there is a need for supervision, i.e. to tell when something is being done right or wrong. In the computing world, this is called **supervised learning**, which these models which we are dealing with here undertake. Therefore, we are now able to see a correlation between a human and a system that acts like a human - how a human learns and how a system that tries to mimic a human learns e.g. when to say what, what is the right answer in this context, etc.

More specifically we are interested in processing and producing language and sentences thus we will be dealing with **Natural Language Processing** models. 

This is a gist of what we are working with.

## Using OpenAI
[Open AI](https://openai.com/) is an organization that pioneered the field of creating language processing models which they have trained with thousands of data sets (information which they have found all across the internet) and made available to the public for use. Each of these has its unique features but all of them are capable of using for mimicking human interactions and thus make a great 'brain' for a virtual assistant. Thus I have chosen this provider for my project.

There are numerous tools and models on their site. A very interesting one happens to be [Assitance AI](https://platform.openai.com/docs/assistants/overview) (which is also one of their latest releases currently in its Beta version). This is geared to be a one-stop solution for creating a virtual assistant for your needs - with a set of models and tools to support it. However, this is a very sophisticated solution that also happens to be charged we look for other alternatives. In practice too this may not be the best tool for a robust solution as it's not heavily tried and tested yet.

Upon searching further I have found a best-suited solution for my project. The [Chat Completions API](https://platform.openai.com/docs/guides/text-generation/chat-completions-api)! With this:
1. I can cater to my basic need of text generation - passing a conversation string and getting back a good response.
2. Not a beta software so it is fairly robust.
3. it is free of charge and easy to use!

Thus my choice for the project prototype.

## Architecture




https://platform.openai.com/docs/api-reference/authentication

## Environment Setup and Executing Code
This section discusses how to set up and run the project.
This is a Python-based implementation, which has been developed over Ubuntu. Run the following to set up Python and its dependencies, and also OpenAI libraries.

```
sudo apt update
sudo apt install python3
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget

sudo apt install python3-pip
pip install --upgrade openai 
```

![image](https://github.com/DeepanwitaR/VirtualAssistant/assets/24522364/f1231454-11de-478c-86f1-9bb6d0bbbbd0)

