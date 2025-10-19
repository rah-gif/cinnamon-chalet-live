from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views  # Import from main app only

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('rooms/', views.rooms, name='rooms'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)