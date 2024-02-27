
from django.contrib import admin
from django.urls import path, include
from main.views import index_page
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('choose/', index_page),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('users/', include('users.urls')),
]
