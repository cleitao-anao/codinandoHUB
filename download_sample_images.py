import os
import requests
from pathlib import Path

def download_image(url, filename):
    """Baixa uma imagem da URL e salva no diretório especificado."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Cria o diretório se não existir
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Salva a imagem
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Imagem baixada: {filename}")
        return True
    except Exception as e:
        print(f"Erro ao baixar a imagem {url}: {e}")
        return False

def main():
    # URLs das imagens de exemplo (imagens de domínio público do Unsplash)
    sample_images = {
        'flowers.jpg': 'https://images.unsplash.com/photo-1490750967868-88aa4486ec95?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80',
        'gift-card.jpg': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80',
        'fireworks.jpg': 'https://images.unsplash.com/photo-1567427017947-545c5f8d16ad?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80',
        'portfolio.jpg': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80',
        'scheduling.jpg': 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80',
        'todo.jpg': 'https://images.unsplash.com/photo-1551033406-611cf9a28f67?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80',
    }
    
    # Diretório de destino
    base_dir = Path(__file__).parent.absolute()
    images_dir = base_dir / 'static' / 'portfolio' / 'images'
    
    print(f"Baixando imagens para: {images_dir}")
    
    # Baixa cada imagem
    for filename, url in sample_images.items():
        filepath = images_dir / filename
        download_image(url, filepath)
    
    print("\nImagens baixadas com sucesso!")
    print("Execute 'python manage.py migrate' e depois 'python populate_db.py' para popular o banco de dados.")

if __name__ == '__main__':
    main()
