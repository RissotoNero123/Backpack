from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:pk>', views.get_blog()),
]
