from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('hub/', views.ProjectListView.as_view(), name='hub'),
    path('project/<int:project_id>/like/', views.like_project, name='like_project'),
    path('project/<int:project_id>/register_view/', views.register_project_view, name='register_project_view'),
    path('project/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
]
