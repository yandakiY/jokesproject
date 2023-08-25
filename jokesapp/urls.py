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
    # Category
    path('categories', views.IndexCategory.as_view() , name="categories"),
    path('create_cat', views.create_cat , name="create_cat"),
    path('post_create_cat', views.post_create_cat , name="post_create_cat"),
    path('<int:cat_id>/update_cat', views.update_cat , name="update_cat"),
    path('<int:cat_id>/post_update_cat', views.post_update_cat , name="post_update_cat"),
    path('<int:cat_id>/delete_cat', views.delete_cat , name="delete_cat"),
    # Joke by categories
    path('<int:cat_id>/display_joke_by_category' , views.display_joke_by_category, name="display_joke_by_category")
]
