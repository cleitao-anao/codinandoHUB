# Codinando - Plataforma de Portfólios

Bem-vindo ao **Codinando**, uma plataforma onde os membros da comunidade podem compartilhar e descobrir projetos incríveis!

## 🚀 Recursos

- **Exibição em Grid**: Visualize projetos em um layout de grade responsivo
- **Detalhes do Projeto**: Páginas dedicadas para cada projeto com estatísticas
- **Interatividade**: Sistema de visualizações e curtidas
- **Interface Moderna**: Design limpo e responsivo com Tailwind CSS
- **Painel Administrativo**: Gerenciamento fácil de projetos

## 🛠️ Tecnologias

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript
- **Estilização**: Tailwind CSS
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Hospedagem de Imagens**: Sistema de arquivos local

## 🚀 Como Executar Localmente

1. **Clonar o repositório**
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   cd codinando-projeto
   ```

2. **Criar e ativar um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar o banco de dados**
   ```bash
   python manage.py migrate
   ```

5. **Criar um superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

7. **Acessar o site**
   - Site: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📦 Estrutura do Projeto

```
codinando-projeto/
├── codinando/               # Configurações do projeto Django
├── portfolio/               # Aplicação principal
│   ├── migrations/          # Migrações do banco de dados
│   ├── static/              # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/           # Templates HTML
│   ├── __init__.py
│   ├── admin.py            # Configuração do painel de administração
│   ├── apps.py             # Configuração da aplicação
│   ├── models.py           # Modelos de dados
│   ├── urls.py             # URLs da aplicação
│   └── views.py            # Visualizações
├── media/                  # Arquivos de mídia enviados pelos usuários
├── static/                 # Arquivos estáticos coletados
├── templates/              # Templates base
├── .gitignore
├── manage.py
└── README.md
```

## 🌐 Deploy

### Requisitos para Produção
- Python 3.8+
- PostgreSQL
- Servidor web (Nginx/Apache)
- Servidor WSGI (Gunicorn/uWSGI)

### Passos para Deploy
1. Configurar variáveis de ambiente
2. Configurar banco de dados PostgreSQL
3. Coletar arquivos estáticos
4. Configurar servidor web
5. Configurar servidor WSGI

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`)
4. Faça o push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ✨ Agradecimentos

- [Django](https://www.djangoproject.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Font Awesome](https://fontawesome.com/)
- [Alpine.js](https://alpinejs.dev/)
