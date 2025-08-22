from django.http import HttpResponse
import datetime
def index(request):
    now = datetime.datetime.now()
    return HttpResponse("<h2> Site is working! </h2> <h3> It is now %s </h3> <a href='/admin' > ADMIN page </a>" % now
        
    )