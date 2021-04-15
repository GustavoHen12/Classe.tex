from django.urls import path
from . import views

app_name = 'texToPdf'
urlpatterns = [
    path(r'^generatePdf/novo', views.generate, name='generatePdf'),
]