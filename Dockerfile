FROM ubuntu:16.04

RUN apt-get update -y &&\
    apt-get install -y python3-pip python3-dev python3-setuptools \
                        build-essential libmysqlclient-dev libpq-dev curl \
                        vim nginx supervisor ufw
COPY . /apisrv/
WORKDIR /apisrv

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /apisrv/HogWhat/logs &&\
    chmod 777 -R /apisrv/HogWhat/logs


RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY install/hogwhat_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/hogwhat_nginx.conf /etc/nginx/sites-enabled/

# RUN ln install/supervisor.conf /etc/supervisor/conf.d/

RUN pip3 install --upgrade pip --no-cache-dir -r requirements.txt

EXPOSE 8000

# CMD ["/usr/bin/supervisord", "-n"]

CMD ["uwsgi", "--socket", "0.0.0.0:8001", \
              "--wsgi-file", "/apisrv/HogWhat/wsgi_dev.py", \
              "--master", \
              "--die-on-term", \
              "--single-interpreter", \
              "--harakiri", "30", \
              "--reload-on-rss", "512", \
              "--post-buffering-bufsize", "8192", \
              "-b", "65535"]
            #   "--logger", "file:/tmp/uwsgi.log"]


# CMD ["uwsgi", "--http", "0.0.0.0:8001", \
#               "--wsgi-file", "/apisrv/HogWhat/wsgi_dev.py", \
#               "--master", \
#               "--die-on-term", \
#               "--single-interpreter", \
#               "--harakiri", "30", \
#               "--reload-on-rss", "512", \
#               "--post-buffering-bufsize", "8192"]
