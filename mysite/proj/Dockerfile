FROM python:3.10-alpine
COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#RUN pip install --upgrade pip\
# && pip install --no-cache-dir -r requirements.txt
#CMD ["python3", "analyze.py"]
CMD python -m bandit proj/views.py 
CMD python -m pycodestyle --first proj/views.py
 
