FROM python:3.10-alpine
COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install bandit
RUN pip install pycodestyle

CMD python -m bandit views.py;python -m pycodestyle views.py
