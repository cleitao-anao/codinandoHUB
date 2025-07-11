document.addEventListener('DOMContentLoaded', function() {
    // Função para obter o token CSRF
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

    // Adiciona o evento de like aos botões
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const projectId = this.getAttribute('data-project-id');
            const likeCount = this.querySelector('.like-count') || this;
            const icon = this.querySelector('i');
            const isActive = this.classList.contains('active');
            
            // Desabilita o botão temporariamente para evitar múltiplos cliques
            this.disabled = true;
            
            // Atualiza a UI imediatamente para feedback visual
            if (!isActive) {
                this.classList.add('active');
                if (likeCount) {
                    const currentLikes = parseInt(likeCount.textContent) || 0;
                    likeCount.textContent = currentLikes + 1;
                }
                if (icon) {
                    icon.classList.remove('fa-thumbs-up');
                    icon.classList.add('fa-check');
                }
            }
            
            // Envia a requisição para o servidor
            fetch(`/project/${projectId}/like/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                // Atualiza a contagem de likes com o valor retornado pelo servidor
                if (likeCount) {
                    likeCount.textContent = data.likes;
                }
                // Habilita o botão novamente
                this.disabled = false;
            })
            .catch(error => {
                console.error('Erro ao curtir o projeto:', error);
                // Reverte as alterações visuais em caso de erro
                if (!isActive) {
                    this.classList.remove('active');
                    if (likeCount) {
                        const currentLikes = parseInt(likeCount.textContent) || 0;
                        likeCount.textContent = Math.max(0, currentLikes - 1);
                    }
                    if (icon) {
                        icon.classList.add('fa-thumbs-up');
                        icon.classList.remove('fa-check');
                    }
                }
                this.disabled = false;
            });
        });
    });

    // Adiciona efeito de hover nos cards
    document.querySelectorAll('.project-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 8px 15px rgba(138, 43, 226, 0.3)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });
});
