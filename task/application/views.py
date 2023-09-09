from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from datetime import date, datetime, timezone


# Create your views here.

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
    current_day = get_current_day()
    utc_time = datetime.now(timezone.utc)
    
    details = {
                "slack_name": "example_name",
                "current_day": current_day,    
                "utc_time": utc_time,
                "track": utc_time,
                "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
                "github_repo_url": "https://github.com/username/repo",
                "status_code": 200
               }
    return JsonResponse(details, status=status.HTTP_200_OK)
