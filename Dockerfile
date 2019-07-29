FROM python:3.7.3
MAINTAINER padocon@naver.com

COPY . /home
WORKDIR /home
RUN pip install pipenv
RUN pipenv install --system
CMD ["python3", "/home/main.py"]