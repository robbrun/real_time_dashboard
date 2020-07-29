from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import DashboardData
from datetime import datetime
from pytz import UTC

def dashboardCurrentTime(request):
    now = datetime.utcnow()
    # hardcode date 20180101 since that is date in csv/sqlite data
    timestamp = datetime(2018, 1, 1, # date range of data
                         now.hour, now.minute, now.second, 0, UTC)
    return _dashboardRender(request, timestamp)

def dashboardRequestTime(request, hour, minute, second):
    try:
        # hardcoded date but takes in current time from computer. can pass in time with /t= if you wish
        timestamp = datetime(2018, 1, 1, # date range of data
                             int(hour), int(minute),
                             int(second), 0, UTC)
    except ValueError:
        raise Http404('Invalid time requested')
    return _dashboardRender(request, timestamp)

def _dashboardRender(request, timestamp):
    try:
        data = DashboardData.objects.get(timestamp=timestamp)
    except DashboardData.DoesNotExist:
        raise Http404('Could not find {}'.format(timestamp))
    return render(request, 'index.html', {'data': data})
