from celery import shared_task
from datetime import datetime, timedelta, date
from .serializers import RoutineResultSerializer
from .models import Routine, Day, Result

@shared_task
def create_result():
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    today = date.today()
    yesterday = today - timedelta(1)
    day = date.weekday(yesterday)
    day_match_routine_list = Day.objects.filter(day__contains=days[day]).values('routine_id')
    day_match_routine_list = [q['routine_id'] for q in day_match_routine_list]
    routine = Routine.objects.filter(routine_id__in=day_match_routine_list)
    for r in routine:
        if not Result.objects.exists(routine_id=r.routine_id, create_at=yesterday):
            result_data = {
                "routine_id": r.routine_id,
                "result": "NOT",
            }
            result_serializer = RoutineResultSerializer(data = result_data)
            if result_serializer.is_valid():
                result_serializer.save()