# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Flower
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




###########################################################################
def main_page(request):
	flowers = Flower.objects.all()
	#pagination
	paginator = Paginator(flowers, 4)
	page = request.GET.get('page')
	try:
		flowers = paginator.page(page)
	except PageNotAnInteger:
		flowers = paginator.page(1)
	except EmptyPage:
		flowers= paginator.page(paginator.num_pages)
	return render(request, 'shop/main.html', {'flowers': flowers})
  

