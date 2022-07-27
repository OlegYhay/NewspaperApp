from django.urls import path
from .views import ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView, \
    AboutAsView, CommenttCreateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('about_us/', AboutAsView.as_view(), name='about_us'),
    path('create_comments/<pk>/', CommenttCreateView.as_view(), name='create_comments'),
]
