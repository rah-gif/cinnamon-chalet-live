from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    
    
]