
from django.contrib import admin
from django.urls import path, include
from main.views import index_page
from django.views.generic import TemplateView
from trainings.views import create, complete
from trainings.views import delete
from trainings.views import mytrainings
from trainings.views import workspace
from trainings.views import traningedit
from trainings.views import pool

urlpatterns = [
    path('admin/', admin.site.urls),
    path('choose/', index_page),
    path('create/', create),
    path('mytrainings/', mytrainings, name='mytrainings'),
    path('delete/<int:id>/', delete),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('workspace/<int:id>/', workspace, name='workspace'),
    path('users/', include('users.urls')),
    path('traningedit/<int:id>/', traningedit, name='traningedit'),
    path('complete/<int:id>/', complete, name='complete'),
    path('pool/<int:user_id>/', pool, name='pool'),
]
