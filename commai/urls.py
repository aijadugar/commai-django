from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Now correctly includes login view and auth paths from 'app.urls'
    path('services/text_interaction/', views.text_interaction, name='text_interaction'),
    path('ask', views.ask, name = 'ask'),
    path('services/speech_interaction/', views.speech_interaction, name='speech_interaction'),
    path('services/daily_tasks/', views.daily_tasks, name='daily_tasks'),
    path('submit_writing_exercise/', views.submit_writing_exercise, name='submit_writing_exercise'),
    path('submit_speaking_exercise/', views.submit_speaking_exercise, name='submit_speaking_exercise'),
    path('partners/partners/', views.partners, name='partners'),
    path('contactus/contactus/', views.contactus, name='contactus'),
]
