from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.catalog, name="catalog"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^cart/remove/$', views.removefromcart, name="remove"),
)
