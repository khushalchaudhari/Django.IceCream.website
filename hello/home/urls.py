from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    # path('admin/', admin.site.urls),
    path("about", views.about, name='about'),
    path("servicesiceCream", views.servicesiceCream, name='servicesiceCream'),
    path("servicessofty", views.servicessofty, name='servicessofty'),
    path("servicesfamilyPack", views.servicesfamilyPack, name='servicesfamilyPack'),
    path("contact", views.contact, name='contact'),
]