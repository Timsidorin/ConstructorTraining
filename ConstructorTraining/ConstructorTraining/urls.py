
from django.contrib import admin
from django.urls import path
from  main import views
from main.views import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page)
]
