from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages


def home(request):
    #todo - make better cookie message
    request.session.set_test_cookie()
    
    context = {
        "item": 1

    }


    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')