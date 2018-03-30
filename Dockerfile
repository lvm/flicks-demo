FROM alpine:edge
MAINTAINER Mauro <mauro@sdf.org>

ENV LIBRARY_PATH=/lib:/usr/lib

ADD [".", "/srv/flicks/"]
COPY ["init-scripts/api.run", "/etc/service/api/run"]
COPY ["init-scripts/admin.run", "/etc/service/admin/run"]

RUN touch /etc/inittab \
    && apk --update add ca-certificates python3 runit \
    && python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --upgrade pip setuptools \
    && if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \
    && if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
    && rm -r /root/.cache \
    && rm -rf /var/cache/apk/* \
    && pip install -r /srv/flicks/requirements.pip \
    && chmod 755 /etc/service/api/run \
    && chmod 755 /etc/service/admin/run \
    && python /srv/flicks/startup.py --init

EXPOSE 8001
EXPOSE 8002
EXPOSE 8003

CMD ["/sbin/runsvdir", "-P", "/etc/service"]
