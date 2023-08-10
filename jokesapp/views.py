from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
def Index(request):
    return HttpResponse("Index Page")