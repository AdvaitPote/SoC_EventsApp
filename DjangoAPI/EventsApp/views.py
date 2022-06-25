from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EventsApp.models import Events
from EventsApp.serializers import EventSerializer

# Create your views here.
@csrf_exempt
def eventApi(request, id=0):
    if request.method=="GET":
        events = Events.objects.all()
        events_serializer = EventSerializer(events, many=True)
        return JsonResponse(events_serializer.data, safe=False)
    
    elif request.method=="POST":
        event_data = JSONParser().parse(request)
        event_serializer = EventSerializer(data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse("Event Added Successfully", safe=False)
        return JsonResponse("Failed to add Event", safe=False)
    
    elif request.method=='PUT':
        event_data = JSONParser().parse(request)
        event = Events.objects.get(EventId=event_data['EventId'])
        event_serializer = EventSerializer(event, data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse("Event Updated Successfully", safe=False)
        return JsonResponse("Failed to update Event", safe=False)

    elif request.method=='DELETE':
        event = Events.objects.get(EventId=id)
        event.delete()
        return JsonResponse("Event Deleted Successfully", safe=False)






