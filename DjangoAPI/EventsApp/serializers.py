from rest_framework import serializers
from EventsApp.models import Events

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('EventId',
                  'EventName',
                  'DateOfEvent',
                  'TimeOfEvent')   