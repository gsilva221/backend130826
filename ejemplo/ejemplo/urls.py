from django.contrib import admin
from django.urls import path, include
from primerapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('primerapp/',include("primerapp.urls")),
    path('segundapp/',include("segundapp.urls"))
]
