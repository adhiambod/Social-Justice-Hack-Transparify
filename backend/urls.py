from django.contrib import admin
from django.urls import path
from backend.transparify import views  # Import views correctly

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.home, name='home'),  # Home page
    path('about/', views.about_us, name='about_us'),  # About page
    path('mission-vision/', views.mission_vision, name='mission_vision'),  # Mission and Vision page
]
