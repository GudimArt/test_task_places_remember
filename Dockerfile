FROM python:3
WORKDIR /app
ADD . ./ 
RUN pip install -r requirements.txt