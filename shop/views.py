# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Flower




###########################################################################
def main_page(request):
	flowers = Flower.objects.all()
	return render(request, 'shop/main.html', {'flowers': flowers})
  

