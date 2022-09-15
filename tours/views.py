from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Hotel
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView,UpdateView



class ListHotel(ListView):
    template_name = 'tours/hotels.html'
    model = Hotel
    # context_object_name = 'feedback'

    # def get_queryset(self):
    # фильтрует данные
    #     queryset=super().get_queryset()
    #     filter_qs = queryset.filter(rating__gt=4)
    #     return filter_qs

# def allhotels(request):
#     all = Hotel.objects.all()
#     return render(request, 'tours/hotels.html', context={'all_hotels': all})



class DetailHotel(DetailView):
    template_name = 'tours/info_about_hotel.html'
    model = Hotel
    # или можно задать свое имя
    # context_object_name = 'feed'


# def get_info_about_hotel(request, id_hotel: int):
    # description = Hotel.objects.get(id=id_hotel)
    # благодаря get_object_or_404 можно эту строчку записать по другому:
    # description = get_object_or_404(Hotel, id=id_hotel)
    # return render(request, 'tours/info_about_hotel.html', context={'description': description})
