from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', views.ArticleEditView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
]
