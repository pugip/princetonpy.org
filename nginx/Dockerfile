FROM nginx
COPY app.conf /etc/nginx/nginx.conf
RUN /bin/bash -c "mkdir -p /var/www/princetonpy.org/{pages,staticfiles}"
COPY pages/ /var/www/princetonpy.org/pages/