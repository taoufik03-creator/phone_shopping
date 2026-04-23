from django.shortcuts import render

# Create your views here.

from django.views.generic import *
from .models import Phone
from .forms import PhoneForm

class PhoneListView(ListView):
    template_name="phones.html"
    queryset=Phone.objects.all()

class PhoneDetailView(DetailView):
    template_name="phone.html"
    queryset=Phone.objects.all()

class PhoneCreateView(CreateView):
    template_name="phone_create.html"
    queryset=Phone.objects.all()
    form_class=PhoneForm

class PhoneUpdateView(UpdateView):
    template_name="phone_update.html"
    queryset=Phone.objects.all()
    fields=["phone_title","phone_brand","phone_model","phone_price"]