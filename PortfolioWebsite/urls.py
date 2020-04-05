# from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PortfolioWebsiteHomepage, name='ViewsHomepage'),
    path("about", views.AboutPage, name = "About"),
    path("contact", views.ContactPage, name = 'Contact'),
    path("portfolio", views.PortfolioPage, name = "Portfolio")

]
