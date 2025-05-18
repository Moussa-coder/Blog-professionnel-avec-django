from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('categorie/<int:id>/', views.articles_par_categorie, name='articles_par_categorie'),
    path('tag/<int:id>/', views.articles_par_tag, name='articles_par_tag'),

]