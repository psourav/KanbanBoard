from django.shortcuts import render,redirect
from kanban.models import Issues
# Create your views here.

def index(request):
    iss = Issues.objects.get.all()
    if request.method == "POST":
        if "add" in request.POST:
            desc = request.POST["desc"]
            priority = request.POST["priority"]
            bklog = Issues(desc=desc, status= 'Backlog', priority = priority)
            bklog.save()
            return redirect('/')
        if "delete" in request.POST:
            desc = request.POST["desc"]
            bklog = Issues.objects.filter(id= desc)
            bklog.delete()

    return render(request, "index.html", iss )