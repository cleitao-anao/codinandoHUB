import os
import sys
import django
from django.utils import timezone
import random
import shutil
from django.conf import settings

# Configuração do ambiente Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codinando.settings')
django.setup()

from portfolio.models import Project

def create_sample_projects():
    # Limpar dados existentes
    print("Limpando dados existentes...")
    Project.objects.all().delete()
    
    # Configurar caminhos
    base_dir = settings.BASE_DIR
    images_dir = os.path.join('portfolio', 'images')
    static_images_dir = os.path.join('static', images_dir)
    media_images_dir = os.path.join('media', 'project_thumbnails')
    
    # Criar diretório de mídia se não existir
    os.makedirs(os.path.join(base_dir, media_images_dir), exist_ok=True)
    
    # Listar imagens disponíveis
    available_images = []
    if os.path.exists(os.path.join(base_dir, static_images_dir)):
        available_images = [f for f in os.listdir(os.path.join(base_dir, static_images_dir)) 
                          if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    print(f"Imagens disponíveis: {available_images}")
    
    # Projetos de exemplo com imagens disponíveis
    projects_data = [
        {
            'title': 'Cartão Presente',
            'author': 'Carlos Oliveira',
            'description': 'Sistema de gerenciamento de cartões presentes virtuais.',
            'access_link': 'https://example.com/gift-card',
            'thumbnail': 'gift-card.jpg' if 'gift-card.jpg' in available_images else None,
            'views': random.randint(100, 1000),
            'likes': random.randint(10, 500)
        },
        {
            'title': 'Fogos de Artifício',
            'author': 'Mariana Santos',
            'description': 'Simulação de fogos de artifício com JavaScript.',
            'access_link': 'https://example.com/fireworks',
            'thumbnail': 'fireworks.jpg' if 'fireworks.jpg' in available_images else None,
            'views': random.randint(100, 1000),
            'likes': random.randint(10, 500)
        },
        {
            'title': 'Portfólio Digital',
            'author': 'João Pereira',
            'description': 'Modelo de portfólio digital responsivo.',
            'access_link': 'https://example.com/portfolio',
            'thumbnail': 'portfolio.jpg' if 'portfolio.jpg' in available_images else None,
            'views': random.randint(100, 1000),
            'likes': random.randint(10, 500)
        },
        {
            'title': 'Sistema de Agendamento',
            'author': 'Fernanda Costa',
            'description': 'Plataforma de agendamento online para serviços diversos.',
            'access_link': 'https://example.com/scheduling',
            'thumbnail': 'scheduling.jpg' if 'scheduling.jpg' in available_images else None,
            'views': random.randint(100, 1000),
            'likes': random.randint(10, 500)
        },
        {
            'title': 'App de Tarefas',
            'author': 'Ricardo Almeida',
            'description': 'Aplicativo de gerenciamento de tarefas com notificações.',
            'access_link': 'https://example.com/todo-app',
            'thumbnail': 'todo.jpg' if 'todo.jpg' in available_images else None,
            'views': random.randint(100, 1000),
            'likes': random.randint(10, 500)
        },
    ]
    
    print("Criando projetos de exemplo...")
    for project_data in projects_data:
        # Criar o projeto sem a miniatura primeiro
        thumbnail = project_data.pop('thumbnail', None)
        project = Project.objects.create(**project_data)
        
        # Se houver uma miniatura, copiar para o diretório de mídia
        if thumbnail:
            try:
                # Caminho de origem (dentro do diretório static)
                src_path = os.path.join(base_dir, static_images_dir, thumbnail)
                
                # Caminho de destino (dentro do diretório media)
                dest_path = os.path.join(base_dir, media_images_dir, thumbnail)
                
                # Copiar o arquivo
                if os.path.exists(src_path):
                    shutil.copy2(src_path, dest_path)
                    
                    # Atualizar o campo de miniatura
                    project.thumbnail.name = f'project_thumbnails/{thumbnail}'
                    project.save()
                    print(f"Miniatura copiada: {thumbnail}")
                else:
                    print(f"Aviso: Arquivo de miniatura não encontrado: {src_path}")
            except Exception as e:
                print(f"Erro ao copiar a miniatura {thumbnail}: {e}")
    
    print(f"Criados {len(projects_data)} projetos de exemplo com sucesso!")

if __name__ == '__main__':
    print("Iniciando a população do banco de dados...")
    create_sample_projects()
    print("População do banco de dados concluída!")
