from django.conf import settings
from django.db import models

from django.contrib import admin
from django.utils import timezone


class User(models.Model):
    user_nom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    etat = models.CharField(max_length=255)


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_nom', 'email', 'telephone', 'password', 'etat')


class Categorie(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.libelle


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description')
    list_filter = ('libelle', 'description')
    search_fields = ['libelle', 'description']


class Produit(models.Model):
    libelle = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prix = models.FloatField(default=0.0)
    qte = models.IntegerField(default=0, verbose_name='Quantité')
    date = models.DateTimeField(default=timezone.now())
    image = models.CharField(max_length=255)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle + ' ' + str(self.prix)


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'description', 'prix', 'qte', 'date')
    list_filter = ('categorie', 'qte', 'date', 'prix')
    ordering = ('libelle', 'date', 'qte')
    search_fields = ['libelle', 'qte', 'prix']
