from django.urls import path
from .views import *

urlpatterns = [
    #Url Ventas
    path('', VentasView.as_view()),
    path('create/', VentasCreate.as_view()),
    path('update/<int:pk>/', VentasUpdate.as_view()),
    path('delete/<int:pk>/', VentasDelete.as_view()),
    path('all/', VentasViewOwner.as_view()),
]