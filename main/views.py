from django.shortcuts import render

# Create your views here.
def start(requests):
    return render(requests, 'start.html')