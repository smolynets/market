# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render




###########################################################################
def main_page(request):
  return render(request, 'shop/new.html', {})

