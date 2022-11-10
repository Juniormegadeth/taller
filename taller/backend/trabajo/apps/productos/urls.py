from django.urls import path
from apps.productos.views import *


app_name = "productos"
urlpatterns = [
     path('', ProductosView.as_view()),
    path('create/', ProductosCreate.as_view()),
    path('update/<int:pk>/', ProductosUpdate.as_view()),
    path('delete/<int:pk>/', ProductosDelete.as_view()),
    path('all/', ProductosViewOwner.as_view()),
]
