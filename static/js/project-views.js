document.addEventListener('DOMContentLoaded', function() {
    // Função para registrar visualização
    function registerProjectView(projectId, projectLink, event) {
        // Previne o comportamento padrão do link
        event.preventDefault();
        
        // Primeiro, tenta registrar a visualização
        fetch(`/project/${projectId}/register_view/`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken')
            },
            credentials: 'same-origin'
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Atualiza o contador de visualizações na página
                const viewsElement = document.querySelector(`.project-card[data-project-id="${projectId}"] .views`);
                if (viewsElement) {
                    viewsElement.textContent = ` ${data.views}`;
                }
            }
            // Abre o link em uma nova aba
            window.open(projectLink, '_blank');
        })
        .catch(error => {
            console.error('Erro ao registrar visualização:', error);
            // Se houver erro, abre o link de qualquer forma
            window.open(projectLink, '_blank');
        });
    }

    // Função auxiliar para obter o cookie CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Adiciona os manipuladores de eventos aos botões de visualização
    document.querySelectorAll('.project-link[data-project-id]').forEach(link => {
        link.addEventListener('click', function(e) {
            const projectId = this.getAttribute('data-project-id');
            const projectLink = this.getAttribute('href');
            registerProjectView(projectId, projectLink, e);
        });
    });
});
