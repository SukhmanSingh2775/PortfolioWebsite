from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def PortfolioWebsiteHomepage(request):
    return render(request, 'MainHomepage.html')


def AboutPage(request):
    context = {"about_page": "active"}
    return render(request, 'AboutPage.html', context)

def ContactPage(request):
    context = {"contact_page": "active"}
    return render(request, 'ContactPage.html',context)

def PortfolioPage(request):
    context = {"portfolio_page": "active"}
    return render(request, 'PortfolioPage.html', context)