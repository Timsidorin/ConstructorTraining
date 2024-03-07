from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponseNotFound
from trainings.models import Training
from django.contrib.auth.models import User
def mytrainings(request):
    author = request.user.id
    trainings = Training.objects.filter(author=author)

    return render(request, "mytrainings.html", {"trainings": trainings})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        training = Training()
        training.title = request.POST.get("title")
        training.describe = request.POST.get("describe")
        training.author = request.user.id
        training.logo = request.FILES.get("logo")
        training.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        training = Training.objects.get(id=id)

        if request.method == "POST":
            training.title = request.POST.get("title")
            training.describe = request.POST.get("describe")
            training.author = request.POST.get("user")
            training.logo = request.FILES.get("logo")
            training.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"training": training})
    except Training.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:

        training = Training.objects.get(id=id)
        training.delete()
        return HttpResponseRedirect("/")
    except Training.DoesNotExist:
        return HttpResponseNotFound("<h2>Training not found</h2>")


def workspace(request, id):
    author = request.user.id
    trainings = Training.objects.filter(author=author)
    return render(request, "workspace.html", {"trainings": trainings})

