from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import date, datetime, timezone


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
