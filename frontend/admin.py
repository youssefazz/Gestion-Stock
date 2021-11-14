from django.contrib import admin
from frontend.models import User, UserAdmin, Produit, ProduitAdmin, Categorie, CategorieAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Categorie, CategorieAdmin)
