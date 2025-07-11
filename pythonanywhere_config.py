# Configurações para o PythonAnywhere

# Configuração do banco de dados (será preenchida no painel do PythonAnywhere)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seu_usuario$nome_do_banco',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha_do_banco',
        'HOST': 'seu_usuario.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# Configurações de arquivos estáticos e mídia
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configurações de segurança
DEBUG = False
ALLOWED_HOSTS = ['seu-usuario.pythonanywhere.com', 'www.seu-dominio.com']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
