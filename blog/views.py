from django.shortcuts import get_object_or_404, render
from .models import Article, Tag

# Create your views here.
def accueil(request):
    articles = Article.objects.filter(statut='publié').order_by('-date_publication')
    return render(request, 'blog/accueil.html', { 'articles':articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, statut='publie')
    commentaires = article.commentaires.filter(approuve=True)
    return render(request, 'blog/article_detail.html', {'article': article, 'commentaires': commentaires})

def articles_par_categorie(request, id):
    categorie = get_object_or_404(id=id)
    articles = Article.objects.filter(categorie=categorie, statut='publie').order_by('-date_publication')
    return render(request, 'blog/articles_par_categorie.html', {
        'categorie': categorie,
        'articles': articles
    })
    
def articles_par_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    articles = Article.objects.filter(tags=tag, statut='publie').order_by('-date_publication')
    return render(request, 'blog/articles_par_tag.html', {
        'tag': tag,
        'articles': articles
    })