from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4><center>నమస్కారం , మీరు పోల్స్ ఇండెక్స్‌లో ఉన్నారు.</center></h4> <br> <h1><center>Hello World. You're at the polls index.</center?</h1>")