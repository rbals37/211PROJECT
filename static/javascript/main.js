import utils from './utils.js'

// 1. 캔버스 불러오기
const canvas = document.querySelector('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const ctx = canvas.getContext('2d');

// 2. Particle 클래스 정의
class Particle {
  constructor(x, y, radius, velocity) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.velocity = velocity;
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
    ctx.fillStyle = '#fff';
    ctx.fill();
    ctx.closePath();
  }

  animate() {
    if (this.x < 0 || this.x > innerWidth || this.y < 0 || this.y > innerHeight) {
      this.x = utils.randomFloatBetween(0, innerWidth);
      this.y = utils.randomFloatBetween(0, innerHeight);
    }

    (mouse.isActive ? particles.concat(mouse) : particles).forEach(particle => {
      const distance = utils.distance(particle.x, particle.y, this.x, this.y);
      if (distance < 200) {
        const from = { x: this.x, y: this.y };
        const to = { x: particle.x, y: particle.y };
        new Line(from, to, distance).draw();
      }
    });

    this.x += this.velocity.x;
    this.y += this.velocity.y;

    this.draw();
  }
}

class Line {
  constructor(from, to, distance) {
    this.from = from;
    this.to = to;
    this.distance = distance;
  }

  draw() {
    ctx.beginPath();
    ctx.moveTo(this.from.x, this.from.y);
    ctx.lineTo(this.to.x, this.to.y);
    ctx.strokeStyle = `rgba(0, 0, 0, ${1- this.distance / 200})`;
    ctx.lineWidth = 1;
    ctx.stroke();
  }
}

// 3. 파티클 만들기
const TOTAL = 200;
let particles = [];
let mouse = { x: 0, y: 0, isActive: false };
for (let i = 0; i < TOTAL; i++) {
  const x = utils.randomFloatBetween(0, innerWidth);
  const y = utils.randomFloatBetween(0, innerHeight);
  const radius = utils.randomFloatBetween(0.5, 2);
  const velocity = {
    x: utils.randomFloatBetween(-2, 2),
    y: utils.randomFloatBetween(-2, 2),
  };
  particles.push(new Particle(x, y, radius, velocity));
}

// 4. 매 프레임마다 실행되는 재귀함수
function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  particles.forEach(particle => particle.animate());

  window.requestAnimationFrame(render);
}

// 5. 윈도우 resize 함수 정의
window.addEventListener('resize', () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});


// chatGPT
// 마우스 이벤트를 윈도우에서 처리 (캔버스의 점 효과를 위해)
window.addEventListener('mousemove', e => {
  const rect = canvas.getBoundingClientRect();
  mouse.x = e.clientX - rect.left; // 캔버스 내에서의 X 좌표
  mouse.y = e.clientY - rect.top;  // 캔버스 내에서의 Y 좌표
  mouse.isActive = true;
});

window.addEventListener('mouseenter', () => mouse.isActive = true);
window.addEventListener('mouseleave', () => mouse.isActive = false);

// 6. 실행하기
render();
