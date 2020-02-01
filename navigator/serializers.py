from .models import Events, Classes, Professor
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['name', 'description', 'location', 'from_date', 'to_date', 'room']


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['subject', 'Day', 'professor', 'start', 'end']


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name', 'description']
