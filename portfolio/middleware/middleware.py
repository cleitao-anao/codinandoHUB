from django.shortcuts import redirect
from django.contrib import messages

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se o caminho começa com /admin/
        if request.path.startswith('/admin/'):
            # Se o usuário não estiver autenticado, deixa o Django lidar com o redirecionamento para o login
            if not request.user.is_authenticated:
                return self.get_response(request)
                
            # Se o usuário estiver autenticado mas não for superusuário
            if not request.user.is_superuser:
                messages.error(request, 'Acesso negado. Apenas administradores podem acessar esta área.')
                return redirect('portfolio:home')
        
        # Para todas as outras requisições, continue normalmente
        response = self.get_response(request)
        return response
