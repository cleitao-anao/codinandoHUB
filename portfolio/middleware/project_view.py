from django.utils import timezone
from portfolio.models import Project

class ProjectViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Verifica se a requisição é para a página de detalhes de um projeto
        if request.path.startswith('/project/') and request.path.endswith('/') and request.path.count('/') == 3:
            try:
                slug = request.path.split('/')[2]
                project = Project.objects.get(slug=slug)
                project.increment_views()
            except (Project.DoesNotExist, IndexError, ValueError):
                pass
                
        return response
