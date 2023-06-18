import random

from django.shortcuts import render

# Create your views here.

def monday (request):
    todo_1 = 'поесть'
    todo_2 = 'поиграть'
    todo_3 = 'выгулить брата'
    return render(request, "monday.html", {'todo_1':todo_1,'todo_2':todo_2,'todo_3':todo_3})

def thuersday (request):
    todo_list = ['выгулить брата',"посмотреть кашу","оскорбить коммунистов","поигарть в роблокс"]
    random.shuffle(todo_list)
    return render(request, "thuersday.html",{'todo_list':todo_list})

def main (request):
    return render (request, "main.html")
