FROM python:3.10-alpine
COPY . .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install bandit
RUN pip install pycodestyle
# && pip install --no-cache-dir -r requirements.txt
#CMD ["python3", "analyze.py"]
CMD python -m bandit views.py 
CMD python -m pycodestyle views.py
 
