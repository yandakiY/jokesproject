from django.urls import path
from . import views

app_name = "jokesapp"

urlpatterns = [
    # index pages (Joke and category)
    path('' , views.Index.as_view() , name="Index"),
    path('categories', views.IndexCategory.as_view() , name="categories"),
    # Path Joke
    path('create', views.create , name="create"),
    path('post_create' , views.post_create , name="post_create"),
    path('<int:joke_id>/update' , views.update , name="update"),
    path('<int:joke_id>/post_update' , views.post_update , name="post_update"),
    path('<int:joke_id>/delete' , views.delete , name="delete"),
    # Jokes in corbeille
    path('jokes_deleted' , views.IndexJokeRemove.as_view() , name="joke_deleted"),
    # Category
    path('create_cat', views.create_cat , name="create_cat"),
    path('post_create_cat', views.post_create_cat , name="post_create_cat"),
    path('<int:cat_id>/update_cat', views.update_cat , name="update_cat"),
    path('<int:cat_id>/post_update_cat', views.post_update_cat , name="post_update_cat"),
    path('<int:cat_id>/delete_cat', views.delete_cat , name="delete_cat"),
    # Categories in corbeille
    path('categories_deleted' , views.IndexCategoryRemove.as_view() , name="categories_deleted"),
    # Joke by categories
    path('<int:cat_id>/display_joke_by_category' , views.display_joke_by_category, name="display_joke_by_category"),
    # remove element - path
    path('<int:cat_id>/remove_cat', views.remove_cat , name="remove_cat"),
    path('<int:joke_id>/remove_joke', views.remove_joke , name="remove_joke"),
    # restore element - path
    path('<int:cat_id>/restore_cat', views.restore_cat , name="restore_cat"),
    path('<int:joke_id>/restore_joke', views.restore_joke , name="restore_joke"),
    # search a joke by word
    path('search_joke' , views.search_joke_by_word, name="search_joke")
    
]
