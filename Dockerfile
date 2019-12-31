FROM alpine:edge
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk add --update python3 python3-dev py3-numpy py3-pandas py3-numpy-dev
RUN apk add --update sqlite
ENV PYTHONPATH /usr/lib/python3.8/site-packages
ENV POETRY_VERSION=0.12.17
RUN pip3 install --upgrade pip && pip3 install poetry==$POETRY_VERSION
ENTRYPOINT ["python3"]