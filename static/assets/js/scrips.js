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