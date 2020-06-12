from django.conf.urls import url, include
from .views import all_products, guitars, keyboards, percussion, product_detail, guitar_detail

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^guitars/$', guitars, name='guitars'),
    url(r'^(?P<pk>\d+)/$', guitar_detail, name='guitar_detail'),
    url(r'^keyboards/$', keyboards, name='keyboards'),
    url(r'^percussion/$', percussion, name='percussion'),
]


