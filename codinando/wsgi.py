"""
WSGI config for codinando project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codinando.settings')

# Cria a aplicação WSGI do Django
django_app = get_wsgi_application()

# Configura o WhiteNoise para servir arquivos estáticos
app = WhiteNoise(django_app, root='staticfiles')
app.add_files('static', prefix='static/')
app.add_files('media', prefix='media/')

# O Vercel espera uma variável 'app' ou 'handler'
application = app
handler = app  # Para compatibilidade com o Vercel
