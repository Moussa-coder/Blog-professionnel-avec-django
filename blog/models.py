from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nom
    
class Tag(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nom
    
class Article(models.Model):
    STATUT_CHOICES = (
        ('brouillon', 'Brouillon'),
        ('publie', 'Publié'),
    )
    
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_publication = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='brouillon')

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
        

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approuve = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.article.titre}"
    
    
class ProfilAuteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)

    def __str__(self):
        return self.user.username
