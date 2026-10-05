from django.urls import path

from courses.views import about, home

app_name= "courses"

urlpatterns = [
    path("", home, name="home"),
    path("sobre/", about, name="about")
]