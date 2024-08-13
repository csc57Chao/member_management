
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Team Member Management Application'),
    path('list/', views.list, name='List Team Members'),
    path('add_form/', views.add_form, name='add_form'),
    path('edit_form/', views.edit_form, name='edit_form'),

]
