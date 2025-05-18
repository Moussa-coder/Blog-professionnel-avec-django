from django.shortcuts import get_object_or_404, render
from .models import Article

# Create your views here.
def accueil(request):
    articles = Article.objects.filter(statut='publié').order_by('-date_publication')
    return render(request, 'blog/accueil.html', { 'articles':articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, statut='publie')
    commentaires = article.commentaires.filter(approuve=True)
    return render(request, 'blog/article_detail.html', {'article': article, 'commentaires': commentaires})