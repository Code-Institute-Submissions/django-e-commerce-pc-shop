from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.urls import reverse_lazy, reverse
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


def get_context_data(self, *args, **kwargs):
    context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
    stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    total_likes = stuff.total_likes()
    context["total_likes"] = total_likes
    return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')
