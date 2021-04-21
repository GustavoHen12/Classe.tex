from django.urls import path
from . import views

app_name = 'texToPdf'
urlpatterns = [
    path(r'^generatePdf/', views.generate, name='generatePdf'),
]