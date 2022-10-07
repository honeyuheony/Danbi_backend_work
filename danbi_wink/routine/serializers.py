from rest_framework import serializers
from .models import Routine, Routine_day, Routine_result


class RoutineDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine_day
        fields = '__all__'

class RoutineResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine_result
        fields = '__all__'

class RoutineSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="account_id")
    
    class Meta:
        model = Routine
        fields = ["routine_id", "id", "title", "category", "goal", "is_alarm"]
