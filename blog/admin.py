from django.contrib import admin
from .models import Article, Categorie, Tag, Commentaire, ProfilAuteur

@admin.register(Article) #La ligne `@admin.register(Commentaire)` est un décorateur fourni par Django pour simplifier l’enregistrement d’un modèle dans l’interface d’administration.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication', 'statut')
    list_filter = ('statut', 'categorie', 'tags')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)} #est un dictionnaire qui indique à Django de remplir automatiquement le champ slug à partir du champ titre. 

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'article', 'date', 'approuve')
    list_filter = ('approuve', 'date')
    search_fields = ('nom', 'message')

@admin.register(ProfilAuteur)
class ProfilAuteurAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)

admin.site.register(Categorie)
admin.site.register(Tag)
