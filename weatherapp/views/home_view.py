
from django.shortcuts import render, HttpResponse

def home_view_render(request):
    return HttpResponse("hey this is home")