from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.index_page),
    path('about_us/', views.about_us_page),
    path('about_us/info/', views.about_us_info)
]
