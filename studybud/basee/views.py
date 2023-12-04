from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

def home(request):
    action = request.GET.get('action') if request.GET.get('action') != None else ''
    
    rooms = Room.objects.filter(Q(topic__name__icontains=action) |
    Q(name__icontains = action)|
    Q(description__icontains = action))
    
    topics = Topic.objects.all()
    room_count = rooms.count()
    
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'basee/home.html', context)

def room(request, pk):
    
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request, 'basee/room.html', context)

def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'basee/room_form.html',context)

def updateRoom(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance=room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    
    context = {'form': form}
    return render(request, 'basee/room_form.html', context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'basee/delete.html', {'obj': room})













