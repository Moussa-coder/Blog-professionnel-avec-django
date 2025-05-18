from django.contrib import admin
from .models import Article, Categorie, Tag, Commentaire, ProfilAuteur

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication', 'statut')
    list_filter = ('statut', 'categorie', 'tags')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}

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
