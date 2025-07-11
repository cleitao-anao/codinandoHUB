import os
import sys

# Adiciona o diretório do projeto ao path
INTERP = os.path.expanduser("/home/seu_usuario/venv/bin/python3")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Configura o caminho para o projeto
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

# Importa a aplicação WSGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codinando.settings_prod')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
