document.addEventListener('DOMContentLoaded', function() {
    // Função para adicionar o token CSRF ao cabeçalho das requisições AJAX
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Verifica se a string do cookie começa com o nome que queremos
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Adiciona o evento de clique a todos os botões de like
    document.querySelectorAll('.like-button').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const likeUrl = this.href;
            const likeCountElement = this.querySelector('.like-count');
            const icon = this.querySelector('i');
            
            // Desabilita o botão temporariamente para evitar múltiplos cliques
            this.disabled = true;
            
            // Adiciona o token CSRF ao cabeçalho da requisição
            const csrftoken = getCookie('csrftoken');
            
            fetch(likeUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                credentials: 'same-origin',
            })
            .then(response => response.json())
            .then(data => {
                // Atualiza a contagem de likes
                if (likeCountElement) {
                    likeCountElement.textContent = data.likes;
                }
                
                // Adiciona uma classe de animação
                icon.classList.remove('far');
                icon.classList.add('fas', 'text-red-500', 'animate-ping');
                
                // Remove a animação após um curto período
                setTimeout(() => {
                    icon.classList.remove('animate-ping');
                }, 500);
            })
            .catch(error => {
                console.error('Erro ao curtir o projeto:', error);
            })
            .finally(() => {
                // Reativa o botão
                this.disabled = false;
            });
        });
    });
});
