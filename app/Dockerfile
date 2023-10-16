FROM alpine:3.18

RUN apk update && apk add --no-cache supervisor python3 py3-pip

RUN adduser appster -D
USER appster
WORKDIR /home/appster/app

ADD requirement.txt /home/appster/app
RUN pip install -r requirement.txt

ADD . /home/appster/app
COPY supervisord.conf /etc/supervisord.conf
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
