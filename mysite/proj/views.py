from django.shortcuts import render
from django.http import HttpResponse
from .models import predmet, uchet
import sqlite3
# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def plswork(request):
    query = predmet.objects.all()
    query1 = uchet.objects.all()
    print(request)
    return render(request, 'proj/index.html', {"predmet":query,
                                               "uchet": query1
                                               })

def mygod():
    connection = sqlite3.connect('db.sqlite3')
    print(connection)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM proj_spektakl")
    records = cursor.fetchall()
    num = (len(records))
    return num

