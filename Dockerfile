FROM ubuntu:latest # TODO: try using a smaller image like alpine. 

ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt-get -y install python3 && apt-get -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget curl && apt-get install -y python3-pip
RUN pip install --upgrade openai
RUN pip install -U Flask

# create non-root user to run flask and thus OpenAI
ARG USER=virtualasst
RUN useradd -ms /bin/bash $USER

# set the user
USER $USER

# set working directory
WORKDIR /home/$USER/

COPY virtualasst.py ./
COPY information.txt ./

ENV OPENAI_API_KEY="<your OPENAI_API_KEY value>"
EXPOSE 8000

ENTRYPOINT ["python3", "virtualasst.py"]
