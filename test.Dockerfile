FROM python:latest

LABEL Maintainer="Thomas Roche<thomas.a.roche@gmail.com>"

ARG BUILD_DATE
ARG VCS_REF

COPY . /

WORKDIR /

RUN pip install -r requirements.txt


ENTRYPOINT [ "python3", "./test.py" ]
