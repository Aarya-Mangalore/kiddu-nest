<script>
  import { onMount, tick } from "svelte";

  export let emoji = "❤️";
  export let floatemoji = "❤️";
  export let bgcolor = "#ffe6f2";
  export let clickdisabled = false; // Set to false to disable heart clicks


  let hearts = [];
  let floatingHearts = [];

  function addHearts(event) {
    const { clientX: x, clientY: y, pageY } = event;

    for (let i = 0; i < 4; i++) {
      let heartX = Math.min(Math.max(x, 20), window.innerWidth - 50);
      let heartY = pageY; // Uses pageY to move with scroll

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

      let offsetX = (Math.random() - 0.5) * 200;
      let offsetY = (Math.random() - 0.5) * 200;

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
  /* Make sure body expands with content */
  html, body {
    min-height: 200vh;
    overflow-x: hidden;
  }

  /* Fixed Background */
  .background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: var(--bgcolor);
    overflow: hidden;
    z-index: -2;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Clickable Overlay Moves with Page */
  .click-layer {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100%;
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

  /* Floating Hearts Stay Fixed on Screen */
  .floating-heart {
    position: fixed;
    font-size: 4vmin;
    opacity: 0.6;
    animation: curvedMove 10s infinite ease-in-out, fadeOut 30s ease-out forwards;
  }

  /* Clicked Hearts Move in Curved Path */
  .small-heart {
    position: absolute;
    font-size: 4vmin;
    opacity: 0.6;
    animation: curvedMove 10s infinite ease-in-out, fadeOut 30s ease-out forwards;
  }

  @keyframes curvedMove {
    0% { transform: translate(0, 0); }
    25% { transform: translate(var(--offsetX), var(--offsetY)); }
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

<!-- Fixed Background -->
<div class="background" style="background-color: {bgcolor};">
  <div class="big-heart">{emoji}</div>
</div>

<!-- Clickable Overlay (Moves with Scroll) -->
{#if !clickdisabled}
  <div 
    class="click-layer"
    role="button"
    tabindex="-2"
    on:click={addHearts}
    on:keydown={handleKeydown}
  ></div>
{/if}


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
