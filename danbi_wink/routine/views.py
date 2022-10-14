from django.conf import settings
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.shortcuts import get_object_or_404 as _get_object_or_404
from django.http import Http404
from django.db import transaction
from django.db.models import Prefetch, Q


from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from asgiref.sync import sync_to_async

from datetime import datetime, timedelta, date

from .models import Routine, Day, Result
from .serializers import RoutineSerializer, RoutineDaySerializer, RoutineResultSerializer
import os, shutil, sys

# Main Page

@transaction.atomic
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def routineList(request):
    if request.method == 'GET':
        today = request.query_params['today']
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        y, m, d = map(int, today.split('-'))
        day = date.weekday(date(y, m, d))
        day_match_routine_list = Day.objects.filter(day__contains=days[day]).values('routine_id')
        day_match_routine_list = [q['routine_id'] for q in day_match_routine_list]
        routine = Routine.objects.filter(routine_id__in=day_match_routine_list)
        res = {
            "data" : [],
            "message": {
                "msg": "Routine lookup was successful.",
                "status": "ROUTINE_LIST_OK"
            }
        }
        for r in routine:
            result = Result.objects.filter(Q(routine_id=r.routine_id) \
                & Q(create_at=today))
            result = result.result if result != None else 'NOT'
            iter =  {
                "goal" : r.goal,
                "id" : str(r.account_id),
                "result" : result,
                "title" : r.title
            }
            res['data'].append(iter)
        return Response(res)

    elif request.method == 'POST':
        days = request.data['days']
        request.data['account_id'] = request.user
        request.data.pop('days')
        serializer = RoutineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            routine_id = Routine.objects.all().order_by('-created_at')[0].routine_id
            day_data = {
                'day': str(days),
                'routine_id': routine_id
            }
            day_serializer = RoutineDaySerializer(data=day_data)
            if day_serializer.is_valid():
                day_serializer.save()
                return Response({
                    "data" : {
                        "routine_id": routine_id
                    },
                    "message": {
                        "msg": "You have successfully created the routine.",
                        "status": "ROUTINE_CREATE_OK"
                    }
                })
        return Response(serializer.errors, status=400)


@transaction.atomic
@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def routineDetail(request, routine_id):
    if request.method == 'GET':
        routine = Routine.objects.get(routine_id=routine_id)
        result = Result.objects.filter(routine_id=routine_id).order_by("-create_at")
        result = result[0].result if result != [] else 'NOT'
        days = Day.objects.get(routine_id=routine_id)
        res = {
            "data" : {
                "goal" : routine.goal,
                "id" : routine.account_id,
                "result" : result,
                "title" : routine.title,
                "days": days.day
            },
            "message": {
                "msg": "Routine lookup was successful.",
                "status": "ROUTINE_DETAIL_OK"
            }
        }
        return Response(res)

    elif request.method == 'PATCH':
        routine = Routine.objects.get(routine_id=routine_id)
        day = Day.objects.get(routine_id=routine_id)
        serializer = RoutineSerializer(routine, data=request.data, partial=True)
        if request.data.get("days"):
            day_serializer = RoutineDaySerializer(day, data={"day": request.data["days"]}, partial=True)
            if day_serializer.is_valid():
                day_serializer.save()
            else:
                return Response(day_serializer.errors, status=400)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data" : {
                    "routine_id": routine_id
                },
                "message": {
                    "msg": "The routine has been modified.",
                    "status": "ROUTINE_UPDATE_OK"
                }
            })
        else:
            return Response(serializer.errors, status=400)
        

    elif request.method == 'DELETE':
        routine = Routine.objects.get(routine_id=routine_id)
        routine.is_deleted = True
        result = Result.objects.filter(routine_id=routine_id)
        for r in result:
            r.is_deleted = True
            r.save()
        routine.save()
        return Response({
                "data" : {
                    "routine_id": routine_id
                },
                "message": {
                    "msg": "The routine has been deleted.",
                    "status": "ROUTINE_DELETE_OK"
                }
        })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def routine_result(request):
    if request.method == 'POST':
        routine_id = request.query_params['routine_id']
        result = request.query_params['result']
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        today = date.today()
        day = date.weekday(today)
        if Day.objects.exists(routine_id=routine_id, day__contains=days[day]):
            if Result.objects.exists(routine_id=routine_id, create_at=today):
                r = Result.objects.get(routine_id=routine_id, create_at=today)
                r.result = result
                r.save()
            else:
                result_data = {
                    "routine_id": routine_id,
                    "result": result,
                }
                result_serializer = RoutineResultSerializer(data = result_data)
                if result_serializer.is_valid():
                    result_serializer.save()
                else:
                    return Response(result_serializer.errors, status=400)
            return Response({
                "data" : {
                    "routine_id": routine_id
                },
                "message": {
                    "msg": "You have successfully created the routine_result.",
                    "status": "ROUTINE_RESULT_CREATE_OK"
                }
            })
        else:
            res = {
                "message": {
                        "msg": "This routine cannot be recorded today.",
                        "status": "ROUTINE_RESULT_CREATE_FAILED"
                }
            }
            return Response(res, status=400)