from django.shortcuts import render

from .models import Package
from baseapp import utils


def home(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def ocean_freight(request):
    return render(request, "ocean-freight.html")


def logistic(request):
    return render(request, "logistics.html")


def air_freight(request):
    return render(request, "air-freight.html")


def cargo_express(request):
    return render(request, "cargo-express.html")


def ware_housing(request):
    return render(request, "warehousing.html")


def custom_brokerage(request):
    return render(request, "custom-brokerage.html")


def about(request):
    return render(request, "about.html")


def track(request):
    context = {}
    track_id = request.GET.get("track-id", None)

    if track_id is not None:
        try:
            package = Package.objects.get(track_id__exact=track_id)

            context["package"] = package
        except Package.DoesNotExist:
            context["package"] = None

    else:
        context["package"] = None
    return render(request, "track.html", context)


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")
