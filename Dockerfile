FROM ubuntu:16.04

RUN apt-get update -y &&\
    apt-get install -y build-essential libmysqlclient-dev libpq-dev vim \
                        python3-pip python3-dev python3-setuptools nginx supervisor                         

ENV LANG C.UTF-8
                         
RUN rm -rf apisrv
RUN mkdir apisrv
WORKDIR /apisrv

ADD . /apisrv/

ENV PYTHONUNBUFFERED 1

COPY install/hogwhat_nginx.conf /etc/nginx/sites-available/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \
    rm /etc/nginx/sites-enabled/default &&\    
    ln -s /etc/nginx/sites-available/hogwhat_nginx.conf /etc/nginx/sites-enabled/ && \
    ln install/supervisor.conf /etc/supervisor/conf.d/

RUN pip3 install --upgrade pip --no-cache-dir -r reqs/prod.txt



EXPOSE 8000
