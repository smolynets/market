# -*- coding: utf-8 -*-
from .models import Flower



def is_digit(string):
    if string.isdigit():
       return 1
    else:
        try:
            float(string)
            return None
        except ValueError:
            return None
