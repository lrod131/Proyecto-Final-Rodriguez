from django.urls import path
from .views import *

app_name= 'message'
urlpatterns = [
    path('messages/', MessagesList.as_view(), name="Messages"),
    path('nuevoMensaje/', MessageCreate.as_view(), name="New_message"),
    path('mensajes/<pk>/', MessageDetail.as_view(), name="Message_detail"),
    path('borrar/<pk>', MessageDelete.as_view(), name="Delete_message"),
]
