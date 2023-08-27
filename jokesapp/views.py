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
        return Joke.objects.all().order_by('-date_pub').filter(view = True);
    
# display all joke in corbeille
class IndexJokeRemove(generic.ListView):
    
    template_name = "jokesapp/jokes_remove.html"
    context_object_name = "jokes"
    
    def get_queryset(self):
        return Joke.objects.all().order_by('-date_pub').filter(view = False);


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

# Send Joke in corbeille Joke
def remove_joke(request , joke_id):
    # get joke 
    j = Joke.objects.get(id = joke_id)
    # j = get_object_or_404(Joke , id=joke_id)
    print(j.question)
    j.view = False
    j.save()
    # dont need to add save()
    
    # redirection
    return HttpResponseRedirect(reverse("jokesapp:Index" , args=()))

def restore_joke(request , joke_id):
    # get joke 
    j = Joke.objects.get(id = joke_id)
    # j = get_object_or_404(Joke , id=joke_id)
    # print(j.question)
    j.view = True
    j.save()
    # redirection
    return HttpResponseRedirect(reverse("jokesapp:Index" , args=()))


# Categories views
class IndexCategory(generic.ListView):
    template_name = "jokesapp/lists_categories.html"
    context_object_name = "categories"
    
    def get_queryset(self):
        return Category.objects.all().order_by("libelle").filter(view = True)
    

# display all categories in corbeille
class IndexCategoryRemove(generic.ListView):
    template_name = "jokesapp/categories_remove.html"
    context_object_name = "categories"
    
    def get_queryset(self):
        return Category.objects.all().order_by("libelle").filter(view = False)

def create_cat(request):
    return render(request , "jokesapp/create_category.html")

def post_create_cat(request):
    # get libelle post
    c = Category.objects.create(libelle = request.POST.get("libelle"))
    c.save()
    return HttpResponseRedirect(reverse("jokesapp:categories" , args=()))

def update_cat(request , cat_id):
    # send category which correspond to id
    cat = Category.objects.get(id = cat_id)
    return render(request , "jokesapp/update_category.html" , {"category":cat})

def post_update_cat(request , cat_id):
    # get category which correspond to id
    cat = Category.objects.get(id = cat_id)
    cat.libelle = request.POST.get("libelle")
    cat.save()
    return HttpResponseRedirect(reverse("jokesapp:categories" , args=()))


def delete_cat(request , cat_id):
    # /get category which corrspond to cat_id
    c = Category.objects.get(id = cat_id)
    c.delete()
    
    return HttpResponseRedirect(reverse("jokesapp:categories" , args=()))

# Send category in corbeille
def remove_cat(request , cat_id):
    # /get category which corrspond to cat_id
    c = Category.objects.get(id = cat_id)
    c.view = False
    c.save()
    
    return HttpResponseRedirect(reverse("jokesapp:categories" , args=()))

# restore catgeory in corbeille
def restore_cat(request , cat_id):
     # /get category which corrspond to cat_id
    c = Category.objects.get(id = cat_id)
    c.view = True
    c.save()
    
    return HttpResponseRedirect(reverse("jokesapp:categories" , args=()))

# views joke by category
def display_joke_by_category(request , cat_id):
    cat = Category.objects.get(id = cat_id)
    joke_for_cat = get_list_or_404(Joke , category = cat)
    
    print(joke_for_cat)
    
    return render(request , "jokesapp/list_joke_by_category.html" , {"jokes":joke_for_cat , "category":cat})