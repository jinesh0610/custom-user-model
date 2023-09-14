from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView, DetailView,DeleteView, CreateView
from articles.models import Article
# Create your views here.

class ArticlesListView(ListView):
    model = Article
    template_name ='article_list.html'
    
class ArticleEditView(UpdateView):
    model = Article
    fields = (
        'title',
        'body',
    )
    template_name = 'article_edit.html'
    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    
    
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    
class ArticleCreateView(CreateView):
    model = Article
    fields = (
        'title',
        'body',
        'author',
    )
    template_name ='article_create.html'
    success_url = reverse_lazy('article_list')