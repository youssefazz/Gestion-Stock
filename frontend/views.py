from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from frontend.models import Produit, Categorie


def main(request):
    return render(request, "main-page.html")


def acceuil(request):
    return render(request, 'acceuil.html')


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main-page')
        else:
            messages.error(request, "login or password incorrect!")
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')
        User.objects.create_user(username=nom, email=email, password=password)
        user = authenticate(username=nom, password=password)
        if user is None:
            return HttpResponse("non authorisé!")
        else:
            return redirect('/main-page')
    return render(request, 'register.html')


def produitList(request):
    produits = Produit.objects.all()
    return render(request, "main-page.html", {"produits": produits})


def getProduit(request):
    produit = Produit.objects.all()
    return render(request, "nouveau-produit.html", {"produits": produit})


def getCategorie(request):
    categorie = Categorie.objects.all()
    return render(request, "nouveau-produit.html", {"categories": categorie})


def getAllProduit(request):
    produits = Produit.objects.all()
    return render(request, "list-produit.html", {"produits": produits})


def ajouterProduit(request):
    if request.method == 'POST':
        libelle = request.POST['libelle']
        description = request.POST['description']
        prix = request.POST['prix']
        quantite = request.POST['quantite']
        date = request.POST['date']
        image = request.POST['image']
        categorie = request.POST['categorie']
        user = request.POST['user']
        if libelle is not None:
            categorie = Categorie(categorie)
            user = User(user)
            produit = Produit.objects.create(libelle=libelle, description=description, prix=prix, qte=quantite,
                                             date=date, image=image, categorie=categorie, user=user)
            produit.save()
            return redirect("/main-page")
        else:
            messages.error(request, "saisir les données du produit")
    produits = Produit.objects.all()
    categories = Categorie.objects.all()
    users = User.objects.all()
    return render(request, "nouveau-produit.html", {"produits": produits, "categories": categories, "users": users})


def deleteProduit(request, id):
    produit = get_object_or_404(Produit, pk=id)
    produit.delete()
    return redirect("/All-produit")


def produitDetails(request, id):
    produit = get_object_or_404(Produit, pk=id)
    return render(request, "produit-details.html", {"produit": produit})


def SproduitDetails(request, id):
    produit = get_object_or_404(Produit, pk=id)
    if request.method == 'POST':
        if request.POST['quantiteR'] is not None:
            sortie = request.POST['quantiteR']
            if sortie is not None:
                produit.qte = produit.qte - int(sortie)
                produit.save()
                return redirect("/main-page")
    return render(request, "produit-details1.html", {"produit": produit})


def EproduitDetails(request, id):
    produit = get_object_or_404(Produit, pk=id)
    if request.method == 'POST':
        if request.POST['quantiteE'] is not None:
            entre = request.POST['quantiteE']
            if entre is not None:
                produit.qte = produit.qte + int(entre)
                produit.save()
                return redirect("/main-page")
    return render(request, "produit-details2.html", {"produit": produit})


def searchProduit(request):
    produits=Produit.objects.all()
    if request.method == 'POST':
        libelle = request.POST['search']
        produits = Produit.objects.filter(libelle=libelle)
    return render(request, "list-produit.html", {"produits": produits})


def logoutUser(request):
    logout(request)
    return redirect('/')
