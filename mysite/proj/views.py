from django.shortcuts import render
from django.http import HttpResponse
from .models import car, order
import sqlite3
# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def plswork(request):
    query = car.objects.all()
    query1 = order.objects.all()
    print(request)
    return render(request, 'proj/index.html', {"car":query,
                                               "order": query1
                                               })

def mygod():
    connection = sqlite3.connect('db.sqlite3')
    print(connection)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM proj_car")
    records = cursor.fetchall()
    num = (len(records))
    return num

