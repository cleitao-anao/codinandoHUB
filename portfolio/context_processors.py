def site_info(request):
    """
    Adiciona informações globais do site e o usuário autenticado a todos os templates.
    """
    context = {
        'SITE_NAME': 'Codinando',
        'SITE_DESCRIPTION': 'Descubra e compartilhe projetos incríveis da nossa comunidade',
        'SITE_URL': 'http://localhost:8000',  # Atualize com o domínio real em produção
    }
    
    # Adiciona o usuário ao contexto se estiver autenticado
    if hasattr(request, 'user'):
        context['user'] = request.user
        
    return context
