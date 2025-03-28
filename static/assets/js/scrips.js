document.addEventListener('DOMContentLoaded', function () {
  // Animação de contagem para os números
  const counters = document.querySelectorAll('.counter-number');
  counters.forEach(counter => {
    const target = parseInt(counter.getAttribute('data-count'));
    const duration = 2000; // duração em ms
    const step = Math.ceil(target / (duration / 20)); // atualiza a cada 20ms
    let current = 0;

    const updateCounter = () => {
      current += step;
      if (current > target) {
        current = target;
      }
      counter.textContent = current;

      if (current < target) {
        setTimeout(updateCounter, 20);
      }
    };

    setTimeout(() => updateCounter(), 500); // inicia após 500ms para dar tempo à página carregar
  });

  // Animação de partículas para o CTA (requer particles.js)
  // Verificar se a biblioteca está disponível
  if (typeof particlesJS !== 'undefined') {
    particlesJS('particles-bg', {
      particles: {
        number: { value: 80 },
        color: { value: '#ffffff' },
        opacity: { value: 0.5 },
        size: { value: 3 },
        line_linked: {
          enable: true,
          color: '#ffffff',
          opacity: 0.4
        },
        move: { speed: 3 }
      }
    });
  }

  // Inicialização do Isotope após as imagens carregarem
  window.addEventListener('load', function () {
    const iso = new Isotope('.isotope-container', {
      itemSelector: '.isotope-item',
      layoutMode: 'masonry'
    });

    // Filtros de portfólio
    const filterBtns = document.querySelectorAll('.portfolio-filters li');
    filterBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        const filterValue = this.getAttribute('data-filter');

        // Remove classe ativa de todos os botões
        filterBtns.forEach(item => {
          item.classList.remove('filter-active');
        });

        // Adiciona classe ativa ao botão clicado
        this.classList.add('filter-active');

        // Filtra os itens
        iso.arrange({ filter: filterValue });
      });
    });
  });

  // Adicionar funcionalidade de play/pause para os vídeos
  const videoContainers = document.querySelectorAll('.video-container');
  videoContainers.forEach(container => {
    const video = container.querySelector('video');
    const overlay = container.querySelector('.video-overlay');

    // Reproduzir vídeo ao passar o mouse
    container.addEventListener('mouseenter', () => {
      video.play();
      overlay.style.opacity = '0';
    });

    // Pausar vídeo ao tirar o mouse
    container.addEventListener('mouseleave', () => {
      video.pause();
      overlay.style.opacity = '1';
    });

    // Clicar no ícone para iniciar/pausar
    overlay.addEventListener('click', (e) => {
      e.stopPropagation();
      if (video.paused) {
        video.play();
        overlay.style.opacity = '0';
      } else {
        video.pause();
        overlay.style.opacity = '1';
      }
    });
  });
});

// Configuração do GLightbox para suportar vídeos
if (typeof GLightbox !== 'undefined') {
  const lightbox = GLightbox({
    selector: '.glightbox',
    touchNavigation: true,
    loop: false,
    autoplayVideos: true
  });
}

document.addEventListener('DOMContentLoaded', function () {
  // Seleciona todos os elementos para animar
  const elements = document.querySelectorAll('.fade-in-element');

  // Ativa a animação após um breve atraso
  setTimeout(() => {
    elements.forEach(element => {
      element.classList.add('fade-in-active');
    });
  }, 300);
});

// Função para alternar o tema
document.addEventListener('DOMContentLoaded', function () {
  const chatPanel = document.querySelector('.chat-panel');
  const chatButton = document.querySelector('.chat-button');
  const closeChat = document.querySelector('.close-chat');
  const sendMessage = document.getElementById('send-message');
  const userMessageInput = document.getElementById('user-message');
  const chatMessages = document.querySelector('.chat-messages');
  const notificationBadge = document.querySelector('.notification-badge');
  const optionButtons = document.querySelectorAll('.option-button');

  // Exibir notificação ao carregar
  notificationBadge.style.display = 'flex';

  // Abrir chat
  chatButton.addEventListener('click', function () {
    chatPanel.classList.add('active');
    notificationBadge.style.display = 'none';
  });

  // Fechar chat
  closeChat.addEventListener('click', function () {
    chatPanel.classList.remove('active');
  });

  // Adicionar mensagem do usuário no chat
  function addUserMessage(message) {
    const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    chatMessages.innerHTML += `
          <div class="message-sent">
              <p>${message}</p>
              <span class="message-time">${currentTime}</span>
          </div>
      `;
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Adicionar resposta do bot
  function addBotResponse(message) {
    const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    chatMessages.innerHTML += `
          <div class="message-received">
              <p>${message}</p>
              <span class="message-time">${currentTime}</span>
          </div>
      `;
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Exibir indicador de carregamento
  function showLoading() {
    chatMessages.innerHTML += `
          <div class="message-received loading">
              <p>Digitando</p>
          </div>
      `;
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Remover indicador de carregamento
  function removeLoading() {
    const loadingElement = document.querySelector('.message-received.loading');
    if (loadingElement) {
      loadingElement.remove();
    }
  }

  // Enviar mensagem para a API do Django
  // Substitua a função sendUserMessage por esta versão atualizada
  function sendUserMessage() {
    const message = userMessageInput.value.trim();
    if (!message) return;

    // Adicionar mensagem do usuário
    addUserMessage(message);
    userMessageInput.value = '';

    // Exibir indicador de carregamento
    showLoading();

    // Determinar a URL correta para a API
    // Podemos usar window.location.origin para garantir que estamos no domínio correto
    const apiUrl = `${window.location.origin}/api/chat/`;
    console.log("Enviando mensagem para:", apiUrl);

    // Enviar para a API do Django
    fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        // Incluir o token CSRF se necessário
        // 'X-CSRFToken': getCsrfToken(),
      },
      body: JSON.stringify({ message: message })
    })
      .then(response => {
        console.log("Status da resposta:", response.status);
        if (!response.ok) {
          throw new Error(`Erro na resposta: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        console.log("Dados recebidos:", data);
        removeLoading();
        if (data.response) {
          addBotResponse(data.response);
        } else {
          addBotResponse("Não consegui processar esta solicitação com base no PDF de objetivos de oração. Posso ajudar com algo específico desse material?");
        }
      })
      .catch(error => {
        console.error("Erro detalhado:", error);
        removeLoading();
        addBotResponse("Estou com dificuldade para acessar o material de objetivos de oração. Por favor, tente novamente ou entre em contato com um consultor diretamente.");
      });
  }

  // Função para obter o token CSRF (se necessário)
  function getCsrfToken() {
    const cookieValue = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];
    return cookieValue || '';
  }

  // Gerenciar cliques nos botões de opção
  optionButtons.forEach(button => {
    button.addEventListener('click', function () {
      const option = this.dataset.option;
      let message = "";

      switch (option) {
        case 'sites':
          message = "Gostaria de informações sobre criação de sites";
          break;
        case 'consultoria':
          message = "Quero saber mais sobre suas consultorias digitais";
          break;
        case 'chatbots':
          message = "Quais são os preços dos serviços de chatbot?";
          break;
        case 'prazos':
          message = "Quais são os prazos para entrega dos projetos?";
          break;
        case 'contato':
          message = "Gostaria de falar com um consultor";
          break;
        default:
          return;
      }

      userMessageInput.value = message;
      sendUserMessage();
    });
  });

  // Enviar mensagem ao clicar no botão
  sendMessage.addEventListener('click', sendUserMessage);

  // Enviar mensagem ao pressionar Enter
  userMessageInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      sendUserMessage();
    }
  });
});
document.addEventListener('DOMContentLoaded', function () {
  // Seleciona todos os elementos para animar
  const elements = document.querySelectorAll('.fade-in-element');

  // Ativa a animação após um breve atraso
  setTimeout(() => {
    elements.forEach(element => {
      element.classList.add('fade-in-active');
    });
  }, 300);
});

setTimeout(function () {
  var toastContainer = document.getElementById("toast-container");
  if (toastContainer) {
    toastContainer.style.opacity = "0";
    setTimeout(() => toastContainer.remove(), 500); // Remove após o fade-out
  }
}, 5000); // Tempo da mensagem na tela