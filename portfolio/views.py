from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import F
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        return Project.objects.all().order_by('-created_at')

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.increment_views()
        return obj

@require_POST
def like_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project.increment_likes()
    return JsonResponse({'likes': project.likes})

def home(request):
    featured_projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio/home.html', {'featured_projects': featured_projects})
