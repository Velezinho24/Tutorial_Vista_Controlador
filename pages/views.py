from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.

# def homePageView(request):
#     return render(request, 'home.html')

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title": "About us - Online Store",
        "subtitle": "About us",
        "description": "This is an about page ...",
        "author": "Developed by: Your Name",
        })
        return context

class ContactPageView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title": "Contact us - Online Store",
        "subtitle": "Contact us",
        "email": "pepitoperez04@gmail.com",
        "dir": "Carrera 23 # 45-67",
        "cel": "3216549870",
        })
        return context

class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV", "price": 1000},
    {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 1200},
    {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 50},
    {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 200},
    ]

class ProductIndexView(View):
    template_name = 'index.html'
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'show.html'
    def get(self, request, id):
        if not id.isdigit() or int(id) < 1 or int(id) > len(Product.products):
            # If the id is invalid, redirect to the home page
            return HttpResponseRedirect('/')
        viewData = {}
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)