FROM alpine:3.18

RUN apk update && apk add --no-cache supervisor python3 py3-pip
COPY supervisord.conf /etc/supervisord.conf

RUN adduser appster -D
USER appster
WORKDIR /home/appster/app

ADD . /home/appster/app
RUN pip install -r requirement.txt

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]