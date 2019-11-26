from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from core.models import product
# Create your views here.
class ProductListView(ListView):
    model= product
    template_name = "home.html"

class ProductDetailView(DetailView):
     model= product
     template_name = "product_detail.html"
class ProductCreateView(CreateView):
    model= product
    fields = ['name', 'price', 'description']
    template_name = "add_product.html"
    

