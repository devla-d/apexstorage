from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages

from courier.models import Package
from .forms import NewPackageForm
from baseapp import utils
from .decorator import manager_required


def sign_out(request):
    logout(request)
    return redirect("admindashboard")


@manager_required
def dashboard(request):
    context = {
        "packages": Package.objects.all().count(),
        "pending_dev": Package.objects.filter(status=utils.PD).count(),
        "completed_dev": Package.objects.filter(status=utils.DV).count(),
    }
    return render(request, "superadmin/dashboard.html", context)


@manager_required
def packages_list(request):
    packages = Package.objects.all()
    return render(request, "superadmin/packages.html", {"packages": packages})


@manager_required
def packages_detail(request, pk):
    package = get_object_or_404(Package, pk=pk)
    return render(request, "superadmin/package_details.html", {"package": package})


@manager_required
def new_packages(request):
    if request.POST:
        n_form = NewPackageForm(request.POST)

        if n_form.is_valid():
            instance = n_form.save()
            messages.info(request, "Package created")
            return redirect("packages_detail", pk=instance.pk)

    else:
        n_form = NewPackageForm(initial={"track_id": utils.gen_random_ids()})

    return render(
        request,
        "superadmin/newpackage.html",
        {"n_form": n_form},
    )
