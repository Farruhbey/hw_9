"""sayt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shablon.views import get_by_category_id
from shablon.views import get_product
from shablon.views import * 
from shablon.views import CreateGullarView
from shablon.views import CreateKategoriyaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', import_data),
    path('', get_product),
    path("<int:kategoriya_id>/", get_by_category_id, name="get_by_categoes"),
    path('add/',CreateKategoriyaView.as_view()),
    path('adds/',CreateGullarView.as_view())
]
