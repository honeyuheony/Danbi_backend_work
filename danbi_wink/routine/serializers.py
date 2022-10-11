from rest_framework import serializers
from .models import Routine, Day, Result


class RoutineDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Day
        fields = '__all__'

class RoutineResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'

class RoutineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Routine
        fields = ["account_id", "title", "category", "goal", "is_alarm"]

