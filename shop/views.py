from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .forms import ItemForm

from .models import Items, Vendors, StockIn, StockOut


# Create your views here.


def index(request):
    return render(request, "shop/index.html")
    

class ItemsView(ListView):
    model = Items
    template_name = "shop/items.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_form"] = ItemForm()
        return context
    
    def form_valid(self, form):
        form.save()



class VendorsView(ListView):
    model = Vendors
    template_name = "shop/vendor.html"
    context_object_name = "vendors"


class StockinView(ListView):
    model = StockIn
    template_name = "shop/stockin.html"
    context_object_name = "stockin"


class StockOutView(ListView):
    model = StockOut
    template_name = "shop/stockout.html"
    context_object_name = "stockout"

