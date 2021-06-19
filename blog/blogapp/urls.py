from django.urls import path

from .views import HomeView, EntryView, CreateEntryView, UpdatePostView, DeletePostView

urlpatterns = [

    path('',HomeView.as_view(),name="blog-home"),
    path("post/<int:pk>/",EntryView.as_view(),name="entry_detail"),
    path('create_entry/',CreateEntryView.as_view(success_url='/'),name="create_entry"),
    path('post/<int:pk>/update_post/',UpdatePostView.as_view(success_url='/'),name="update_Post"),
    path('post/<int:pk>/delete_post/',DeletePostView.as_view(success_url='/'),name="delete_Post")
]
