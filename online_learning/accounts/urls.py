from django.urls import path
from .views import *

urlpatterns = [
    path('', choices, name="choices"),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('tec_reg/', registration, name="registration"),
]
