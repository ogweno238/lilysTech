from django.shortcuts import render

# Create your views here.

# home
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

# about
def about(request):
    context = {}
    return render(request, 'base/about.html', context)

# contact
def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)