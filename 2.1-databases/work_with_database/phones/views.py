from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    if request.GET['sort'] == 'name':
        phones = Phone.objects.all().order_by('name')
    elif request.GET['sort'] == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    elif request.GET['sort'] == 'min_price':
        phones = Phone.objects.all().order_by('price')
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__exact=slug)
    context = {'phone': phone.first()}
    return render(request, template, context)