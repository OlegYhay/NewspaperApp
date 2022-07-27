from audioop import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView, TemplateView

from .models import Article, Comment


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    login_url = 'login'



class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'body','img']
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        ob = self.get_object()
        if ob.author != self.request.user:
            return redirect(ob)

        return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
    template_name = 'article_delete.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        ob = self.get_object()
        if ob.author != self.request.user:
            return redirect(ob)
        return super(ArticleDeleteView, self).dispatch(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ['title', 'body','img']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AboutAsView(TemplateView):
    template_name = 'About_us.html'


class CommenttCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    login_url = 'login'
    reverse_lazy = 'article_list'
    fields = ['comment']
    template_name = 'comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['pk'])
        return super(CommenttCreateView, self).form_valid(form)
