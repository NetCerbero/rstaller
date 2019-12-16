from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from colector.models import Colector
import datetime
from django.utils import timezone
#from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    return HttpResponse("Hello world you're in index")

#@ensure_csrf_cookie
def log(request):
    if request.method == 'POST':
        date = request.GET.get('date', datetime.datetime.now(tz=timezone.utc))

        user_id = request.POST['user_id']
        content_id = request.POST['content_id']
        event = request.POST['event_type']
        session_id = request.POST['session_id']
        print("el metodo", request)
        l = Colector(
            created=date,
            user_id=user_id,
            content_id=str(content_id),
            event=event,
            session_id=str(session_id))
        l.save()
    else:
        HttpResponse('log only works with POST')

    return HttpResponse('ok')
    
