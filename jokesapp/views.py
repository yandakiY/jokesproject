from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
def Index(request):
    return render(request , "jokesapp/index.html",{"name":"Boa Yandaki Yves Michel"})