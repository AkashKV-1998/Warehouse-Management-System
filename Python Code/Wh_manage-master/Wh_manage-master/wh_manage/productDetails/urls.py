from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^list', views.product_list),
    url(r'path/(?P<value>\d+)/$', views.product_path, name="product_path"),
    url(r'order', views.product_order, name="order"),
    url(r'category', views.category, name="category"),
    url(r'manufacturer', views.manufacturer, name="manufacturer"),
    url(r'suggestions', views.suggestions, name="suggestions"),
    url(r'product', views.product_form, name="product"),
    url(r'^', views.index),
    url(r'pro', views.product_delete, name="pro"),
    
]