from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("sjukt3vlig", views.sjukt3vlig, name= "sjukt3vlig")




]