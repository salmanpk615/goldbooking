from typing import Any, Dict, Optional
from django.db import models
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from django.views.generic import View



from django.template.loader import render_to_string

import qrcode
from django.core.files.base import ContentFile


from weasyprint import HTML

from io import BytesIO
from django.http import HttpResponse




from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, FormView
from .forms import ItemForm, ItemUpdateForm, VendorForm, StockinForm, StockoutForm, ReportForm, ReportUpdateForm, StockinUpdate, StockoutUpdate, VendorUpdateForm, UserCreationForm

from .models import Items, Vendors, StockIn, StockOut, Reports


# Create your views here.

def index(request):
    return render(request, "shop/home.html")


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = "shop/login/"
    template_name = "shop/registration/signup.html"
    

class ItemsView(ListView, FormView):
    model = Items
    template_name = "shop/items.html"
    context_object_name = "items"
    form_class = ItemForm
    success_url = "/shop/items"


    def form_valid(self, form):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(form.instance.qr_code)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code image to the model instance
        img_io = BytesIO()
        img.save(img_io, format='PNG')
        img_file = ContentFile(img_io.getvalue(), f'{form.instance.qr_code}.png')
        form.instance.qr_code.save(f'{form.instance.qr_code}.png', img_file)
        # form.save()
        return super().form_valid(form)  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_form"] = ItemForm()
        return context    
    
    
class ItemDelete(DeleteView):
    model = Items
    template_name = "shop/item_delete.html"
    success_url = "/shop/items"
    
    
class ItemEdit(UpdateView):
    model = Items
    form_class = ItemUpdateForm
    template_name = "shop/item_update.html"
    success_url = "/shop/items"  


class VendorsView(ListView, FormView):
    model = Vendors
    template_name = "shop/vendor.html"
    context_object_name = "vendors"
    form_class = VendorForm
    success_url = "/shop/vendors"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vendor_form"] = VendorForm()
        return context
   

class VendorEdit(UpdateView):
    model = Vendors
    form_class = VendorUpdateForm
    template_name = "shop/vendors_update.html"
    success_url = "/shop/vendors" 



class VendorDelete(DeleteView):
    model = Vendors
    template_name = "shop/vendor_delete.html"
    success_url = "/shop/vendors"


class StockinView(ListView, FormView):
    model = StockIn
    template_name = "shop/stockin.html"
    context_object_name = "stockin"
    form_class = StockinForm
    success_url = "/shop/stockin"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stockin_form"] = StockinForm()
        return context
    
    
def slip_view(request, pk):
	items = StockIn.objects.filter(pk=pk)
	return render(request, 'shop/slipin.html', {
        'items': items,
        })
    

class StockinEdit(UpdateView):
    model = StockIn
    form_class = StockinUpdate
    template_name = "shop/stockin_update.html"
    success_url = "/shop/stockin" 




class StockinDelete(DeleteView):
    model = StockIn
    template_name = "shop/stockin_delete.html"
    success_url = "/shop/stockin"



class StockOutView(ListView, FormView):
    model = StockOut
    template_name = "shop/stockout.html"
    context_object_name = "stockout"
    form_class = StockoutForm
    success_url = "/shop/stockout"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stockout_form"] = StockoutForm()
        return context


def slip_out(request, pk):
	items = StockOut.objects.filter(pk=pk)
	return render(request, 'shop/slipout.html', {
        'items': items,
        })

class StockOutEdit(UpdateView):
    model = StockOut
    form_class = StockoutUpdate
    template_name = "shop/stock_update.html"
    success_url = "/shop/stockout" 


class StockoutDelete(DeleteView):
    model = StockOut
    template_name = "shop/stockout_delete.html"
    success_url = "/shop/stockout"


class ReportsView(ListView, FormView):
    model = Reports
    template_name = "shop/reports.html"
    context_object_name = "reports"
    form_class = ReportForm
    success_url = "/shop/reports"


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_form"] = ReportForm()
        return context
    

def pdf_view(request, pk): 
    items = Reports.objects.filter(pk=pk)
    html_string = render(request, 'shop/pdf.html', {'items': items}).content.decode('utf-8')
    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="my_pdf_file.pdf"'
    return response


class ReportDelete(DeleteView):
    model = Reports
    template_name = "shop/report_delete.html"
    success_url = "/shop/reports"
    
    
class ReportEdit(UpdateView):
    model = Reports
    form_class = ReportUpdateForm
    template_name = "shop/report_update.html"
    success_url = "/shop/reports"

