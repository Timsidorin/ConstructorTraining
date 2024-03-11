from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import TrainingEditForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from .models import Coordinates
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponseNotFound
from trainings.models import Training
from django.http import JsonResponse
import json
import  datetime
from django.views.decorators.csrf import csrf_exempt
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
    try:
        training = get_object_or_404(Training, id=id)
        return render(request, "workspace.html", {"training": training})
    except Training.DoesNotExist:
        return HttpResponseNotFound("<h2>Training not found</h2>")


def traningedit(request, id):
    training = get_object_or_404(Training, id=id)
    if request.method == 'POST':
        form = TrainingEditForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            messages.success(request, 'Training edited successfully.')
            # Перенаправление на страницу complete с id тренировки
            return redirect(reverse('complete', kwargs={'id': id}))
    else:
        form = TrainingEditForm(instance=training)  # Preload existing title
    return render(request, "traningedit.html", {"form": form, "training": training})


def complete(request, id):
    try:
        training = get_object_or_404(Training, id=id)
        return render(request, "complete.html", {"training": training})
    except Training.DoesNotExist:
        return HttpResponseNotFound("<h2>Training not found</h2>")

def pool(request, user_id):
    try:
        author = request.user.id
        User = get_user_model()
        user = User.objects.get(id=user_id)
        return render(request, "pool.html", {"user": user, "author": author})
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>User not found</h2>")


def save_coordinates(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        object_id = data.get('object_id')
        top = data.get('top')
        left = data.get('left')
        width = data.get('width')
        height = data.get('height')


        if not all([top, left, width, height]):
            return JsonResponse({'error': 'Missing data'}, status=400)


        try:
            if object_id:
                coordinates = Coordinates.objects.get(id=object_id)
                coordinates.top = top
                coordinates.left = left
                coordinates.width = width
                coordinates.height = height
                coordinates.save()
            else:
                coordinates = Coordinates.objects.create(top=top, left=left, width=width, height=height)

            # Возвращаем id объекта в ответе
            return JsonResponse({'success': 'Coordinates saved or updated', 'object_id': coordinates.id})

        except Coordinates.DoesNotExist:
            return JsonResponse({'error': 'Object not found'}, status=404)
        except IntegrityError as e:
            return JsonResponse({'error': str(e)}, status=400)