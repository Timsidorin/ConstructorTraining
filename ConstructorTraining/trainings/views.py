from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect, HttpResponseNotFound
from trainings.models import Training

def my_trainings(request):
    training = Training.objects.all()
    return render(request, "index.html", {"training": training})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        training = Training()
        training.title = request.POST.get("title")
        training.describe = request.POST.get("describe")
        training.save()
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        training = Training.objects.get(id=id)

        if request.method == "POST":
            training.title = request.POST.get("title")
            training.describe = request.POST.get("describe")
            training.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": training})
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