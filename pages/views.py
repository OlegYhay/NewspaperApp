from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from articles.models import Article


class HomePageView(ListView):
    template_name = 'home.html'
    model = Article
    context_object_name = 'articles'
    def get_queryset(self):
        return Article.objects.all()[:2]

