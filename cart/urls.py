
from django.conf.urls import url
from . import views
from shopdb.settings import MEDIA_ROOT, DEBUG
from django.conf.urls.static import static
from django.conf import settings
from shop.views import FlowerDelete



urlpatterns = [
    
    url(r'^add/(?P<flower_id>\d+)/$', views.CartAdd, name='CartAdd'),
    url(r'^basket', views.basket, name='basket'),
    url(r'^ad/(?P<flower_id>\d+)/$', views.CartAdd_basket, name='CartAdd_basket'),
    url(r'^remove/(?P<flower_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^oformlenya_zamovlenya/', views.OrderCreate, name='OrderCreate'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)