FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /local;
ADD /app /local
RUN mkdir /config
ADD /config/requirements.txt /config
RUN pip install -r /config/requirements.txt
EXPOSE 8888
CMD bash -c "python manage.py makemigrations && python manage.py migrate && gunicorn lpbc.wsgi --reload -b 0.0.0.0:8888"
WORKDIR /local
