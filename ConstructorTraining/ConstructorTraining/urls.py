
from django.contrib import admin
from django.urls import path, include
from main.views import index_page
from django.views.generic import TemplateView
from trainings.views import create
from trainings.views import delete
from trainings.views import mytrainings
from trainings.views import workspace


urlpatterns = [
    path('admin/', admin.site.urls),
    path('choose/', index_page),
    path('create/', create),
    path('mytrainings/', mytrainings),
    path('delete/<int:id>/', delete),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('workspace/', workspace),

    path('users/', include('users.urls')),
]
