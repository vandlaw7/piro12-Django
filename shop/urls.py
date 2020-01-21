from django.urls import path, register_converter

from . import views
from .converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('archives/<yyyy:year>/', views.archives_year, name='archives_year'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('new/', views.item_new, name='item_new'),
    path('<int:pk>/edit', views.item_edit, name='item_edit'),
]
