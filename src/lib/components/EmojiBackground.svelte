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
      hearts = [
        ...hearts,
        {
          id: Date.now() + i,
          x,
          y,
          offsetX: (Math.random() - 0.5) * 300,
          offsetY: (Math.random() - 0.5) * 300,
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
      floatingHearts = [
        ...floatingHearts,
        {
          id: Date.now(),
          x: Math.random() * window.innerWidth,
          y: Math.random() * window.innerHeight,
          offsetX: (Math.random() - 0.5) * 500,
          offsetY: (Math.random() - 0.5) * 500,
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
  /* Main Background */
  .background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: var(--bgcolor);
    overflow: hidden;
    z-index: -2; /* Behind everything */
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Clickable Overlay (Curtain Effect) */
  .click-layer {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 2; /* Brings it to the front */
  }

  .big-heart {
    font-size: 70vmin;
    opacity: 0.6;
    animation: beat 1.5s infinite alternate ease-in-out;
  }

  @keyframes beat {
    0% { transform: scale(1); }
    100% { transform: scale(1.1); }
  }

  .small-heart, .floating-heart {
    position: absolute;
    font-size: 4vmin;
    opacity: 0.6;
    animation: curvedMove 10s infinite ease-in-out, fadeOut 30s ease-out forwards;
  }

  @keyframes curvedMove {
    0% { transform: translate(0, 0); }
    25% { transform: translate(calc(var(--offsetX) * 0.5), calc(var(--offsetY) * 0.5)); }
    50% { transform: translate(calc(var(--offsetX) * -1), calc(var(--offsetY) * -1)); }
    75% { transform: translate(var(--offsetX), var(--offsetY)); }
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

<!-- Clickable Overlay (Now Emoji Clicks Work!) -->
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
    style="
      left: {heart.x}px; 
      top: {heart.y}px;
      --offsetX: {heart.offsetX}px;
      --offsetY: {heart.offsetY}px;
      --scale: {heart.scale};
    "
  >
    {heart.emoji}
  </div>
{/each}

{#each floatingHearts as heart (heart.id)}
  <div 
    class="floating-heart" 
    style="
      left: {heart.x}px; 
      top: {heart.y}px;
      --offsetX: {heart.offsetX}px;
      --offsetY: {heart.offsetY}px;
      --scale: {heart.scale};
    "
  >
    {heart.emoji}
  </div>
{/each}
