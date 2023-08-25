from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_list_or_404 , get_object_or_404
from .models import Joke , Category
from django.views import generic
from django.urls import reverse
from django.utils import timezone

# Create your views here.
class Index(generic.ListView):
    
    template_name = "jokesapp/index.html"
    context_object_name = "jokes"
    
    def get_queryset(self):
        return Joke.objects.all().order_by('-date_pub');
    

# views create jokes page 
def create(request):
    # we need to send list of category in this page
    list_cat = Category.objects.all();
    print(list_cat)
    return render(request , "jokesapp/create.html" , {"categories":list_cat})

# post method for create jokes page 
def post_create(request):
    # print(request.POST.get("category"))
    # print(request.POST.get("question"))
    # print(request.POST.get("answer"))
    # print(timezone.now())
    
    # get category eq to cat
    cat = Category.objects.get(id = request.POST.get("category"))
    
    # jokes , created = Joke.objects.get_or_create(category=request.POST.get("category") , question=request.POST.get("question") , answer=request.POST.get("answer") , date_pub=timezone.now())
    j = Joke(category=cat , question=request.POST.get("question") , answer=request.POST.get("answer") , date_pub=timezone.now())
    j.save()
    
    return HttpResponseRedirect(reverse("jokesapp:Index" , args=()))


def update(request , joke_id):
    # get joke correspond to id 
    j = Joke.objects.get(id = joke_id)
    print(j.category.id)
    
    list_cat = Category.objects.all();
    print(list_cat)
    return render(request , "jokesapp/update.html" , {"categories":list_cat , "joke":j})

def post_update(request , joke_id):
    # get joke which correspond to id
    j = Joke.objects.get(id = joke_id)
    
    # value of category
    cat = Category.objects.get(id = request.POST.get("category"))
    
    # get joke
    j = get_object_or_404(Joke , id=joke_id)
    
    j.category = cat
    j.question = request.POST.get("question")
    j.answer = request.POST.get("answer")
    
    # save all changes
    j.save()
    
    return HttpResponseRedirect(reverse("jokesapp:Index" , args=()))


def delete(request , joke_id):
    # get joke 
    j = Joke.objects.get(id = joke_id)
    # j = get_object_or_404(Joke , id=joke_id)
    print(j.question)
    j.delete()
    # dont need to add save()
    
    # redirection
    return HttpResponseRedirect(reverse("jokesapp:Index" , args=()))