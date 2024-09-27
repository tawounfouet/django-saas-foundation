from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from visits.models import PageVisit

@login_required
def dashboard_view(request):


    PageVisit.objects.create(path=request.path)
    return render(request, "dashboard/main.html", {})