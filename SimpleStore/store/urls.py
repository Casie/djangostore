from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.catalog, name="catalog"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^cart/remove/$', views.removefromcart, name="remove"),
    url(r'^cart/checkout/$', views.checkout, name="checkout"),
    url(r'^cart/checkout/complete/$', views.completeOrder, name="complete_order"),
    url(r'^admin-login/$', views.adminLogin, name="admin-login"),
    url(r'^admin-panel/$', views.adminDashboard, name="admin"),
)
