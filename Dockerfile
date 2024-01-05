FROM alpine:3.14

COPY virtualasst.py .

# Download the python and related dependencies
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Download flask and openAI python libraries
RUN pip install --upgrade openai && pip install -U Flask

ENV OPENAI_API_KEY=${OPENAI_API_KEY}

ENTRYPOINT ["python3", "virtualasst.py"]