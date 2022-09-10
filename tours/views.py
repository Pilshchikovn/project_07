from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Hotel


def allhotels(request):
    all = Hotel.objects.all()
    return render(request, 'tours/hotels.html', context={'all_hotels': all})


def get_info_about_hotel(request, id_hotel: int):
    # description = Hotel.objects.get(id=id_hotel)
    # благодаря get_object_or_404 можно эту строчку записать по другому:
    description = get_object_or_404(Hotel, id=id_hotel)
    return render(request, 'tours/info_about_hotel.html', context={'description': description})
