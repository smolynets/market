
from django.conf.urls import url
from . import views
from shopdb.settings import MEDIA_ROOT, DEBUG
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    url(r'^$', views.main_page, name='main'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)