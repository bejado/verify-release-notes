FROM python:3.10.4

RUN pip3 install pygithub==1.55

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1

COPY verify_release_notes.py ./

CMD [ "python", "./verify_release_notes.py" ]
