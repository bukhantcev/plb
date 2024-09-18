from django.shortcuts import render

# Create your views here.


def welcome(request):
    print(request.path)

    return render(request, 'main/welcome.html')

def home(request):
    print(request.path)

    return render(request, 'main/home.html')