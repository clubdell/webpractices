from django.shortcuts import render

import socket


# Create your views here.
def home(request):
    server_ip = socket.gethostbyname(request.META['SERVER_NAME'])
    return render(request, 'users/home.html', {'server_ip': server_ip})
