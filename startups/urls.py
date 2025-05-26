from django.urls import path
from . import views

app_name = "startups"
urlpatterns =[
    path("", views.home, name="home"),
    path("bsbs/", views.bsbs, name="bsbs"),
    path("how-it-works/", views.how_it_works, name="how_it_works"),
    path("stalls/<int:category_id>/", views.stalls, name="stalls"),
    path("stall/<int:stall_id>/", views.stall, name="stall"),
    path("create_stall/", views.create_stall, name="create_stall"),
]