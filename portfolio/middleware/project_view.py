class ProjectViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # O middleware não incrementa mais as visualizações aqui
        # A contagem é feita diretamente na view de detalhes
        return self.get_response(request)
