"""
URL configuration for commai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('services/text_interaction/', views.text_interaction, name='text_interaction'),
    path('ask', views.ask, name = 'ask'),
    path('services/speech_interaction/', views.speech_interaction, name = 'speech_interaction'),
    path('services/daily_tasks/', views.daily_tasks, name = 'daily_tasks'),
    path('submit_writing_exercise/', views.submit_writing_exercise, name='submit_writing_exercise'),
    path('submit_speaking_exercise/', views.submit_speaking_exercise, name='submit_speaking_exercise'),
    path('partners/partners/', views.partners, name = 'partners'),
    path('contactus/contactus/', views.contactus, name = 'contactus'),
]
