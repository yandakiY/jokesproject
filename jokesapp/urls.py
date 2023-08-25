from django.urls import path
from . import views

app_name = "jokesapp"

urlpatterns = [
    path('' , views.Index.as_view() , name="Index"),
    path('create', views.create , name="create"),
    path('post_create' , views.post_create , name="post_create"),
    path('<int:joke_id>/update' , views.update , name="update"),
    path('<int:joke_id>/post_update' , views.post_update , name="post_update"),
    path('<int:joke_id>/delete' , views.delete , name="delete"),
]
