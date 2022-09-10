from django.urls import path
from . import views

urlpatterns = {
    path('hotels/', views.allhotels, name='main_page'),
    path('hotels/<int:id_hotel>', views.get_info_about_hotel, name='hotel-detail')
}