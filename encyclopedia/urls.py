from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("/search", views.search, name="search"),
    path("/new", views.create_new_page, name="create_new_page")
]
