// ============================================
// AI Agent Interactive Portfolio Website
// ============================================

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    initLoading();
    initCustomCursor();
    initThreeParticles();
    initTypingEffect();
    initNavigation();
    initMagneticEffects();
    initScrollAnimations();
    initParallax();
});

// ============================================
// Loading Screen
// ============================================
function initLoading() {
    const loadingSteps = [
        '初始化 AI Agent...',
        '載入粒子系統...',
        '配置互動模組...',
        '準備完畢!'
    ];
    
    let step = 0;
    const progress = document.getElementById('loadingProgress');
    const status = document.getElementById('loadingStatus');
    const loadingScreen = document.getElementById('loadingScreen');
    
    const interval = setInterval(() => {
        if (step < loadingSteps.length) {
            status.textContent = loadingSteps[step];
            progress.style.width = ((step + 1) / loadingSteps.length * 100) + '%';
            step++;
        } else {
            clearInterval(interval);
            setTimeout(() => {
                loadingScreen.classList.add('hidden');
                initPageAnimations();
            }, 500);
        }
    }, 600);
}

function initPageAnimations() {
    // Animate hero elements
    gsap.from('.hero-badge', {
        duration: 1,
        y: -50,
        opacity: 0,
        ease: 'power3.out'
    });
    
    gsap.from('.hero-title', {
        duration: 1.2,
        y: 50,
        opacity: 0,
        ease: 'power3.out',
        delay: 0.3
    });
    
    gsap.from('.hero-desc', {
        duration: 1,
        y: 30,
        opacity: 0,
        ease: 'power3.out',
        delay: 0.8
    });
    
    gsap.from('.hero-cta', {
        duration: 1,
        y: 30,
        opacity: 0,
        ease: 'power3.out',
        delay: 1
    });
}

// ============================================
// Custom Cursor
// ============================================
function initCustomCursor() {
    const cursorDot = document.getElementById('cursorDot');
    const cursorRing = document.getElementById('cursorRing');
    
    if (!cursorDot || !cursorRing) return;
    
    let mouseX = 0, mouseY = 0;
    let ringX = 0, ringY = 0;
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        cursorDot.style.left = mouseX + 'px';
        cursorDot.style.top = mouseY + 'px';
    });
    
    function animateRing() {
        ringX += (mouseX - ringX) * 0.15;
        ringY += (mouseY - ringY) * 0.15;
        cursorRing.style.left = ringX + 'px';
        cursorRing.style.top = ringY + 'px';
        requestAnimationFrame(animateRing);
    }
    animateRing();
    
    // Hover effects
    const interactiveElements = document.querySelectorAll('a, button, .magnetic, .portfolio-item, .service-card, .course-item');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => cursorRing.classList.add('hover'));
        el.addEventListener('mouseleave', () => cursorRing.classList.remove('hover'));
    });
}

// ============================================
// Three.js Particle System
// ============================================
function initThreeParticles() {
    const canvas = document.getElementById('threeCanvas');
    if (!canvas) return;
    
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    
    // Create particles
    const particleCount = 200;
    const positions = new Float32Array(particleCount * 3);
    const colors = new Float32Array(particleCount * 3);
    
    for (let i = 0; i < particleCount; i++) {
        positions[i * 3] = (Math.random() - 0.5) * 20;
        positions[i * 3 + 1] = (Math.random() - 0.5) * 20;
        positions[i * 3 + 2] = (Math.random() - 0.5) * 20;
        
        // Gold color variation
        colors[i * 3] = 0.68 + Math.random() * 0.32;
        colors[i * 3 + 1] = 0.5 + Math.random() * 0.3;
        colors[i * 3 + 2] = 0.24 + Math.random() * 0.2;
    }
    
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    
    const material = new THREE.PointsMaterial({
        size: 0.05,
        vertexColors: true,
        transparent: true,
        opacity: 0.8,
        blending: THREE.AdditiveBlending
    });
    
    const particles = new THREE.Points(geometry, material);
    scene.add(particles);
    
    camera.position.z = 5;
    
    // Mouse interaction
    let mouseX = 0, mouseY = 0;
    document.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX / window.innerWidth) * 2 - 1;
        mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
    });
    
    // Animation loop
    function animate() {
        requestAnimationFrame(animate);
        
        particles.rotation.x += 0.001;
        particles.rotation.y += 0.001;
        
        // Respond to mouse
        particles.rotation.x += mouseY * 0.0005;
        particles.rotation.y += mouseX * 0.0005;
        
        renderer.render(scene, camera);
    }
    animate();
    
    // Resize handler
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
}

// ============================================
// Typing Effect
// ============================================
function initTypingEffect() {
    const typingElement = document.getElementById('typingText');
    if (!typingElement) return;
    
    const text = window.SITE_CONFIG?.tagline || '用影像說話，為品牌發聲';
    let index = 0;
    
    function type() {
        if (index < text.length) {
            typingElement.innerHTML = text.substring(0, index + 1) + '<span class="typing-cursor"></span>';
            index++;
            setTimeout(type, 100);
        } else {
            typingElement.innerHTML = text + '<span class="typing-cursor"></span>';
        }
    }
    
    setTimeout(type, 2000);
}

// ============================================
// Navigation
// ============================================
function initNavigation() {
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// ============================================
// Magnetic Effects
// ============================================
function initMagneticEffects() {
    const magnetics = document.querySelectorAll('.magnetic');
    
    magnetics.forEach(el => {
        el.addEventListener('mousemove', (e) => {
            const rect = el.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            el.style.transform = `translate(${x * 0.2}px, ${y * 0.2}px)`;
        });
        
        el.addEventListener('mouseleave', () => {
            el.style.transform = 'translate(0, 0)';
        });
    });
}

// ============================================
// Scroll Animations
// ============================================
function initScrollAnimations() {
    gsap.registerPlugin(ScrollTrigger);
    
    // Animate sections on scroll
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        gsap.from(section, {
            scrollTrigger: {
                trigger: section,
                start: 'top 80%',
                end: 'top 20%',
                scrub: 1
            },
            opacity: 0.3,
            y: 100
        });
    });
}

// ============================================
// Parallax Effect
// ============================================
function initParallax() {
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const heroContent = document.querySelector('.hero-content');
        
        if (heroContent && scrolled < window.innerHeight) {
            heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
            heroContent.style.opacity = 1 - (scrolled / window.innerHeight) * 0.7;
        }
    });
}

// ============================================
// Mobile Menu
// ============================================
function toggleMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    const hamburger = document.getElementById('hamburger');
    
    menu.classList.toggle('active');
    hamburger.classList.toggle('active');
}
