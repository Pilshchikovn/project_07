from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.ListHotel.as_view(), name='main_page'),
    # path('hotels/', views.allhotels, name='main_page'),
    path('hotels/<int:pk>', views.DetailHotel.as_view(), name='hotel-detail'),
    # path('hotels/<int:id_hotel>', views.get_info_about_hotel, name='hotel-detail')
]