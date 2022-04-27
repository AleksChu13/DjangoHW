import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))




def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_num = int(request.GET.get('page', 1))
    with open(BUS_STATION_CSV,  newline='') as stations_csv:
        reader = csv.DictReader(stations_csv)
        stations = list(reader)
        paginator = Paginator(list(stations), 10)
        page = paginator.get_page(page_num)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)