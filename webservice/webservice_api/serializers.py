from rest_framework import serializers
from .models import Webservise, Info, Welcome

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['date', 'time', 'weekday']


class WebserviseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webservise
        fields = ['timestamp', 'user']


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Welcome
        fields = ['greetings', 'user']