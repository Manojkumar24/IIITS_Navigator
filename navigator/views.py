from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Classes, Rooms, Professor, Events
import datetime
from .serializers import EventSerializer, ClassesSerializer, ProfessorSerializer

# Create your views here.
def home(request):
    return render(request, 'navigator/homepage.html')


def floor(request, floor_num):
    rooms = Rooms.objects.filter(floor=floor_num)
    return render(request, 'navigator/firstfloor.html', {'rooms': rooms})


def getEvent(request, loc):
    events = Events.objects.filter(location=loc)
    print(len(events))
    for event in events:
        event_date = str(event.to_date.date()).split('-')
        if (datetime.datetime.today().date() > datetime.date(int(event_date[0]), int(event_date[1]),
                                                             int(event_date[2]))):
            print('deleting....')
            event.delete()

    return render(request, 'navigator/events.html', {'events': events})



@api_view(['GET'])
def eventLocationList(request):
    if request.method == 'GET':
        try:
            if Events.objects.filter(location=request.GET.get('location')).exists():
                snippets = Events.objects.filter(location=request.GET.get('location'))
                serializer = EventSerializer(snippets, many=True)
                return JsonResponse(serializer.data, safe=False)
            return Response('Wrong location', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Wrong location', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def classesList(request):
    if request.method == 'GET':
        try:
            if Classes.objects.filter(room_no__number=request.GET.get('class')).exists():
                snippets = Classes.objects.filter(room_no__number=request.GET.get('class'))
                serializer = ClassesSerializer(snippets, many=True)
                return JsonResponse(serializer.data, safe=False)
            return Response('Wrong class number', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Wrong class number', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def professorDetails(request):
    if request.method == 'GET':
        try:
            if Professor.objects.filter(room__number=request.GET.get('class')).exists():
                snippets = Professor.objects.filter(room__number=request.GET.get('class'))
                serializer = ProfessorSerializer(snippets, many=True)
                return JsonResponse(serializer.data, safe=False)
            return Response('Wrong class number', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Wrong class number', status=status.HTTP_400_BAD_REQUEST)
