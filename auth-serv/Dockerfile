FROM ubuntu:18.04

RUN apt-get update && apt-get -y install python3 python3-pip

EXPOSE 80

ADD ./server/ /server/

RUN python3 -m pip install -r ./server/requirements.txt

CMD python3 /server/server.py
