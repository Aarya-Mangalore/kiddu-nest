<script>
  import { onMount, tick } from "svelte";

  export let emoji = "❤️";
  export let floatemoji = "❤️";
  export let bgcolor = "#ffe6f2";

  let hearts = [];
  let floatingHearts = [];

  function addHearts(event) {
    const { clientX: x, clientY: y } = event;

    for (let i = 0; i < 4; i++) {
      let heartX = Math.min(Math.max(x, 20), window.innerWidth - 50);
      let heartY = Math.min(Math.max(y, 20), window.innerHeight - 50);

      hearts = [
        ...hearts,
        {
          id: Date.now() + i,
          x: heartX,
          y: heartY,
          offsetX: (Math.random() - 0.5) * 100,
          offsetY: (Math.random() - 0.5) * 100,
          scale: Math.random() * 0.8 + 0.5,
          opacity: 0.6,
          emoji: floatemoji
        }
      ];
    }

    tick().then(() => {
      setTimeout(() => {
        hearts = hearts.slice(4);
      }, 30000);
    });
  }

  function generateFloatingHearts() {
    setInterval(() => {
      const maxX = window.innerWidth - 50;
      const maxY = window.innerHeight - 50;

      let x = Math.random() * maxX;
      let y = Math.random() * maxY;

      // Ensure floating hearts stay within bounds
      let offsetX = Math.min(Math.max((Math.random() - 0.5) * 200, -x), maxX - x);
      let offsetY = Math.min(Math.max((Math.random() - 0.5) * 200, -y), maxY - y);

      floatingHearts = [
        ...floatingHearts,
        {
          id: Date.now(),
          x,
          y,
          offsetX,
          offsetY,
          scale: Math.random() * 0.8 + 0.5,
          opacity: 0.6,
          emoji: floatemoji
        }
      ];

      setTimeout(() => {
        floatingHearts = floatingHearts.slice(1);
      }, 30000);
    }, 1000);
  }

  onMount(() => {
    generateFloatingHearts();
  });

  function handleKeydown(event) {
    if (event.key === "Enter" || event.key === " ") {
      addHearts(event);
    }
  }
</script>

<style>
  /* Full Background Cover */
  .background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh; /* Ensures full coverage */
    background-color: var(--bgcolor);
    overflow: hidden;
    z-index: -2;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Clickable Overlay */
  .click-layer {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 2;
  }

  /* Beating Heart */
  .big-heart {
    font-size: 70vmin;
    opacity: 0.6;
    animation: beat 1.5s infinite alternate ease-in-out;
  }

  @keyframes beat {
    0% { transform: scale(1); }
    100% { transform: scale(1.1); }
  }

  /* Floating and Clicked Hearts */
  .small-heart, .floating-heart {
    position: absolute;
    font-size: 4vmin;
    opacity: 0.6;
    animation: curvedMove 10s infinite ease-in-out, fadeOut 30s ease-out forwards;
  }

  @keyframes curvedMove {
    0% { transform: translate(0, 0); }
    25% { transform: translate(max(-50px, min(var(--offsetX), 50px)), max(-50px, min(var(--offsetY), 50px))); }
    50% { transform: translate(max(-100px, min(var(--offsetX), 100px)), max(-100px, min(var(--offsetY), 100px))); }
    75% { transform: translate(max(-50px, min(var(--offsetX), 50px)), max(-50px, min(var(--offsetY), 50px))); }
    100% { transform: translate(0, 0); }
  }

  @keyframes fadeOut {
    0% { opacity: 0.6; }
    100% { opacity: 0; }
  }

  @media (max-width: 600px) {
    .big-heart { font-size: 50vmin; }
  }
</style>

<!-- Main Background -->
<div class="background" style="background-color: {bgcolor};">
  <div class="big-heart">{emoji}</div>
</div>

<!-- Clickable Overlay -->
<div 
  class="click-layer"
  role="button"
  tabindex="0"
  on:click={addHearts}
  on:keydown={handleKeydown}
></div>

{#each hearts as heart (heart.id)}
  <div 
    class="small-heart" 
    style="left: {heart.x}px; top: {heart.y}px;
      --offsetX: {heart.offsetX}px;
      --offsetY: {heart.offsetY}px;
      --scale: {heart.scale};"
  >
    {heart.emoji}
  </div>
{/each}

{#each floatingHearts as heart (heart.id)}
  <div 
    class="floating-heart" 
    style="left: {heart.x}px; top: {heart.y}px;
      --offsetX: {heart.offsetX}px;
      --offsetY: {heart.offsetY}px;
      --scale: {heart.scale};"
  >
    {heart.emoji}
  </div>
{/each}
