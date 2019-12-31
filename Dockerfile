FROM alpine:edge
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk add --update python3 python3-dev py3-numpy py3-pandas py3-numpy-dev
RUN apk add --update sqlite
ENV PYTHONPATH /usr/lib/python3.8/site-packages
RUN pip3 install --upgrade pip
RUN pip3 install requests==2.22.0
RUN pip3 install pytest==5.3.2
RUN pip3 install pandas==0.25.3
RUN pip3 install numpy==1.18.0
RUN pip3 install fastapi==0.45.0
RUN pip3 install poetry==0.12.17
RUN poetry config settings.virtualenvs.create false
# RUN poetry install --no-dev

EXPOSE 80

CMD uvicorn --host 0.0.0.0 --port 80 main:app