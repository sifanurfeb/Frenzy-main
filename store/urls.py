from . import views
from django.urls import path
from django.contrib import admin

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)