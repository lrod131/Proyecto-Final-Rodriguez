from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.home_page),
    path('post/<slug:slug>',views.postDetailView.as_view(),name='post')
]