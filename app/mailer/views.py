#-*- coding: utf-8 -*-

# Create your views here.
from django.views.generic import ListView

from .models import Company

class IndexView(ListView):
    template_name = "mailer/index.html"
    model = Company
    paginate_by = 100
