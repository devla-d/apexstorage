from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("services/ocean-freight/", views.ocean_freight, name="ocean_freight"),
    path("services/logistic/", views.logistic, name="logistic"),
    path("services/air-freight/", views.air_freight, name="air_freight"),
    path("services/cargo-express/", views.cargo_express, name="cargo_express"),
    path("services/warehousing/", views.ware_housing, name="ware_housing"),
    path("services/custom-brokerage/", views.custom_brokerage, name="custom_brokerage"),
    path("about/", views.about, name="about"),
    path("track/", views.track, name="track"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]
