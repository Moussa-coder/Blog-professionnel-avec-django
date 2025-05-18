from django.shortcuts import render
from .models import Article

# Create your views here.
def accueil(request):
    articles = Article.objects.filter(statut='publié').order_by('-date_publication')
    return render(request, 'blog/accueil.html', { 'articles':articles})