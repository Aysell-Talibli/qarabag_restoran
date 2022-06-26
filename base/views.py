from django.shortcuts import render
from .models import Menu, Menu_category, Category,Gallery
from django.utils import translation

from django.conf import settings
from django.shortcuts import redirect
def home(request):
    language='az'
    translation.activate(language)
    if 'language' in request.GET and request.GET['language']:
        language = request.GET['language']
        if language in ['ru','en']:
            if language == 'ru': 
                translation.activate(language)
            if language == 'en': 
                translation.activate(language)
            
    
    menu=Menu.objects.order_by('-pk')[:4]
    return render(request,'index.html',{'menu':menu})
    
    
def menu(request):
    language='az'
    translation.activate(language)
    if 'language' in request.GET and request.GET['language']:
        language = request.GET['language']
        if language in ['ru','en']:
            if language == 'ru': 
                translation.activate(language)
            if language == 'en': 
                translation.activate(language)
    category=request.GET.get('category')
    if(category==None):
        menu=Menu.objects.all()
    else:
        menu=Menu.objects.filter(category__category=category)
    categories=Category.objects.all()
    return render(request,'menu.html',{'menu':menu, 'categories': categories})
    
def gallery(request):
    gallery=Gallery.objects.all()
    language='az'
    translation.activate(language)
    if 'language' in request.GET and request.GET['language']:
        language = request.GET['language']
        if language in ['ru','en']:
            if language == 'ru': 
                translation.activate(language)
            if language == 'en': 
                translation.activate(language)
    return render(request,'gallery.html',{'gallery':gallery})

def contact(request):
    language='az'
    translation.activate(language)
    if 'language' in request.GET and request.GET['language']:
        language = request.GET['language']
        if language in ['ru','en']:
            if language == 'ru': 
                translation.activate(language)
            if language == 'en': 
                translation.activate(language)
    return render(request,'contact.html')