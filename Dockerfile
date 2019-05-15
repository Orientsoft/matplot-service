FROM python:3.6-alpine as base

FROM base as builder
RUN apk --no-cache add \
                       gcc \
                       musl-dev \
                       g++

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install" -r /requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

FROM base
RUN apk --no-cache add \
                       gcc \
                       musl-dev \
                       g++

COPY static/fonts /usr/share/fonts

COPY --from=builder /install /usr/local
WORKDIR /app
COPY . .

CMD [ "python", "run.py" ]
