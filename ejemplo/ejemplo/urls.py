from django.contrib import admin
from django.urls import path
from primerapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('primera/',views.inicio),
    path('ahora/',views.ahora)
]
