import datetime
from django.http import HttpResponse


def index(request):
    now = datetime.datetime.now()
    html = '<h2> Site is working! </h2> <h3> It is now %s </h3> <a href="/admin" > ADMIN page </a>' % now

    return HttpResponse(html)
