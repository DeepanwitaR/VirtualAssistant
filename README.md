# VirtualAssistant
A small project where I created a simple text-based virtual assistant using Gen AI to introduce myself to a user. :)

## Background
A **virtual assistant** is a program that lives on the computer say a website or an application, that interacts with a user like a human being through text or audio. We feel like it is a person answering our questions, except it is a fully independent software system that is acting. Let us understand what it is and thus how will we be bringing one to life.

These can take in audio/text as input from the user, then make sense of the sentence with context and relevance and finally produce text/audio to give a meaningful response. How is this possible? **Machine learning** - the science of teaching a computer system to mimic human thoughts and responses. This is done through maths and logic, which enables it to process input(by breaking them into small logical pieces of information called vectors), churn out an accepted logical answer (processing through algebra), and learn from each round of calculations(whether an answer was good or not and how can it be made better - error feedback loops). There are many different problems in the world to solve and thus it's helpful to have different approaches to machine learning for each, these are called **machine learning models**. 

Just like humans, there is a need for supervision, i.e. to tell when something is being done right or wrong. In the computing world, this is called **supervised learning**, which these models which we are dealing with here undertake. Therefore, we are now able to see a correlation between a human and a system that acts like a human - how a human learns and how a system that tries to mimic a human learns e.g. when to say what, what is the right answer in this context, etc.

This is a gist of what we are working with.

## Using OpenAI
https://platform.openai.com/docs/assistants/overview 
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

![image](https://github.com/DeepanwitaR/VirtualAssistant/assets/24522364/5c04b6ce-7015-4350-9176-d7eb87757da6)
