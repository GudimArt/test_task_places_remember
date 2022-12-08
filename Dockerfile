FROM python:3
WORKDIR /app
ADD . ./ 
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate