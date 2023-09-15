from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import date, datetime, timezone
from .models import User
from .serializers import UserSerializer
from rest_framework import serializers
from django.shortcuts import get_object_or_404


#geting the current day from the integer values returned from date.today()
def get_current_day():
    today = date.today()

    if today.weekday() == 0:
        day = "Monday"
    elif today.weekday() == 1:
        day = "Tuesday"
    elif today.weekday() == 2:
        day = "Wednesday"
    elif today.weekday() == 3:
        day = "Thursday"
    elif today.weekday() == 4:
        day = "Friday"
    elif today.weekday() == 5:
        day = "Saturday"
    else:
        day = "Sunday"

    return day

@api_view(['GET'])
def get_intern_details(request):
    if request.method == 'GET':
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')
        current_day = get_current_day()
        time = datetime.now(timezone.utc)
        utc_time =  time.replace(microsecond=0)
    
        details = {
                    "slack_name": slack_name,
                    "current_day": current_day,    
                    "utc_time": utc_time,
                    "track": track,
                    "github_file_url": "https://github.com/Tekkieware/HNGx-backend-task1/blob/main/task/application/views.py",
                    "github_repo_url": "https://github.com/Tekkieware/HNGx-backend-task1",
                    "status_code": 200
                }
    return JsonResponse(details, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    user = UserSerializer(data=request.data)
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT', 'DELETE', 'GET'])
def tweak_user(request, **kwargs):
     # get the user id in the path param and find user
    user_id = kwargs.get('user_id')
    user = get_object_or_404(User, pk=user_id)
    print("found")

    if request.method == "GET":
    # if there is a user with the id, return it else raise error
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
                       
    elif request.method == "PUT":
        # if there is a user with the id, update and return it else raise error
        user = UserSerializer(instance=user, data=request.data)
 
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=="DELETE":
        user.delete()
        return Response({"detail": "user successfully deleted"}, status=status.HTTP_200_OK)


