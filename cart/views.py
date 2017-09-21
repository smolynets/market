# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Flower
from .cart import Cart



def CartAdd(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    cart.add(flower=flower, quantity=1)
    return redirect('main')



#######################################################################
