from django.shortcuts import render

def home(request):
    template = 'catapp/home.html'
    return render(request, template)