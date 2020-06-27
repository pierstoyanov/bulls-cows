from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import re
from datetime import datetime


def home(request):

    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match(r'[A-Za-z]', name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
        
    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

    return render(
        request,
        'bulls_cows/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )