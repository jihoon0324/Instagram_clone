from django.urls import path

from .views import Main


app_name="posts"
urlpatterns = [

    path('', Main.as_view() , name="Main"),

]