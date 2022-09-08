from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


places = {
    'Новый Буян - new_buyan': 'Тут информация по Новому Буяну',
    'Русская селитьба - russian_settlement': 'Тут информация по  русской селитьбе',
    'Ягодное - yagodnoe': 'Тут информация по c.Ягодное',

}


def allplaces(request):
    data = {
        'all_trips': list(places),
    }
    return render(request, 'trip/main_page.html', context=data)


# def allplaces(request):
#     return HttpResponse(list(places))




def get_info_about_place(request, each_place: str):
    description = places.get(each_place)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестное место {each_place}')

def get_info_about_place_by_number(request, each_place: int):
    if each_place > len(list(places)):
        return HttpResponseNotFound(f'Был передан не верный порядковый номер {each_place}')
    place_name = list(places)[each_place - 1]
    reverse_redirect_url = reverse('favourite_place', args=(place_name,))
    '''reverse конструирует путь по урлу. Первым параметром название, вторым куда. 
    Args должна быть упорядоченная коллекция, кортеж
    Обращаем внимание в args на то, сколько функция get_info_about_place принимает значений, только должны быть и args
    Args может быть коллекцией список'''
    return HttpResponseRedirect(reverse_redirect_url)


# def get_info_about_place_by_number(request, each_place: int):
#     if each_place > len(list(places)):
#         return HttpResponseNotFound(f'Был передан не верный порядковый номер {each_place}')
#     place_name = list(places)[each_place-1]
#     return HttpResponseRedirect(f'/places/{place_name}')
def buy_tour(request):
    return render(request, 'trip/buy_tour.html')

def free_tour(request):
    return render(request, 'trip/free_tour.html')

# def get_info_about_place(request, each_place):
#     if each_place == 'new_buyan':
#         return HttpResponse('Страница посвященная Новому Буяну')
#     elif each_place == 'russian_settlement':
#         return HttpResponse('Страница посвященная русской селитьбе')
#     elif each_place == 'yagodnoe':
#         return HttpResponse('Страница посвященная c.Ягодное')
#     else:
#         return HttpResponseNotFound(f'Неизвестное место {each_place}')

# def russian_settlement(request):
#     return HttpResponse('Страница посвященная русской селитьбе')
#
#
# def yagodnoe(request):
#     return HttpResponse('Страница посвященная c.Ягодное')
#
#
# def new_buyan(request):
#     return HttpResponse('Страница посвященная Новому Буяну')
