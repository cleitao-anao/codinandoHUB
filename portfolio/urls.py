from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('hub/', views.ProjectListView.as_view(), name='hub'),
]
