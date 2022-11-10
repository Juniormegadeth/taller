from django.urls import path
from .views import *

urlpatterns = [
    #Url Clientes
    path('', ClientesView.as_view()),
    path('create/', ClientesCreate.as_view()),
    path('update/<int:pk>/', ClientesUpdate.as_view()),
    path('delete/<int:pk>/', ClientesDelete.as_view()),
    path('all/', ClientesViewOwner.as_view()),
]