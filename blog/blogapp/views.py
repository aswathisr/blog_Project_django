from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


class HomeView(LoginRequiredMixin,ListView):
    model = Post
    template_name: str = 'blogapp/index.html'
    context_object_name = "blog_posts"
    ordering = ['-date']
    paginate_by = 3

class EntryView(LoginRequiredMixin,DetailView):
    model=Post
    template_name="blogapp/entry_detail.html"

class CreateEntryView(LoginRequiredMixin,CreateView):
    model= Post
    template_name="blogapp/create.html"
    fields=['title','text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin,UpdateView):
    model= Post
    template_name="blogapp/update_post.html"
    fields=['title','text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = Post
    template_name = "blogapp/delete_post.html"

