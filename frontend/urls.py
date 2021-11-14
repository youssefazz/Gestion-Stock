from django.contrib import admin
from django.urls import path, include
from frontend.views import index, register, main, logoutUser, acceuil, produitList, getProduit, getAllProduit, \
    ajouterProduit, deleteProduit, produitDetails, SproduitDetails, EproduitDetails, searchProduit

urlpatterns = [
    path('', view=acceuil, name="acceuil"),
    path('index', view=index, name="login"),
    path('register', view=register, name="register"),
    path('main-page', view=produitList, name="main"),
    path('logout', view=logoutUser, name="logout"),
    path('produit', view=ajouterProduit, name="produit"),
    path('All-produit', view=getAllProduit, name="allProduit"),
    path('delete-produit/<int:id>', view=deleteProduit, name="deleteProduit"),
    path('produit/details/<int:id>', view=produitDetails, name="produitDetails"),
    path('produit/details/entre/<int:id>', view=EproduitDetails, name="EproduitDetails"),
    path('produit/details/sortie/<int:id>', view=SproduitDetails, name="SproduitDetails"),
    path('search', view=searchProduit, name="searchProduit")
]
