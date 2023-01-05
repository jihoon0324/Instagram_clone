from django.urls import path

from .views import Main, UploadPost

app_name = "posts"
urlpatterns = [

    path('', Main.as_view(), name="Main"),
    path('upload', UploadPost.as_view()),
]
