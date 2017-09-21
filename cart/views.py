# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Flower
from .cart import Cart
from .forms import CartAddProductForm



def CartAdd(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    cart.add(flower=flower, quantity=1)
    return redirect('main')

#######################################################################



def basket(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    return render(request, 'shop/basket.html', {'cart': cart})

#####################################################################


def CartAdd_basket(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(flower=flower, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('basket')

#########################################################################

def CartRemove(request, flower_id):
    cart = Cart(request)
    flower = get_object_or_404(Flower, id=flower_id)
    cart.remove(flower)
    return redirect('basket')


#############################################################################
