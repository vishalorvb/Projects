from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    h = "This is variable passed from views"
    data ={'h':h}
    s= render(request, 'testapp/show.html',data)
    return s

def view(request):
    s="<h1>this is view page<h1>"
    return HttpResponse(s)    
    



