from django.shortcuts import render
from django.http.response import HttpResponse

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Design'},
    {'id':3, 'name':'Front end dev'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request, pk):
    room = None
    for r in rooms:
        if r['id'] == int(pk):
            room = r
    context = {'room': room}
    return render(request, 'room.html', context)
