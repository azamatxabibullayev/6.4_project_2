from django.urls import path
from .views import get_info, get_phones, add_phones, detail, update_phones

app_name = 'phones'
urlpatterns = [
    path('', get_info, name='get_info'),
    path('phones/<int:pk>', get_phones, name='get_phones'),
    path('phones/detail/<int:pk>', detail, name='detail'),
    path('add_phones', add_phones, name='add_phones'),
    path('update_phones/<int:pk>/', update_phones, name='update_phones'),
]
