<script>
    import MemoryItem from "$lib/components/Content.svelte";
    import StarBG from "$lib/components/EmojiBackground.svelte"
  
    const memories = [
      {
        image: "/kidu/20240801_160245.jpg",
        text: "The day we laughed till our stomachs hurt ❤️",
      },
      {
        image: "/kidu/1677344538132.jpg",
        text: "Our first adventure together 🌍",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
      {
        image: "/kidu/1684861917780.jpg",
        text: "That magical evening under the stars ✨",
      },
    ];
  </script>
  <StarBG floatemoji="⭐" emoji="✨"/>
  <main class="memory-page">
    <br>
    <h1 class="title">💖 Memory Hall 💖</h1>
  
    <div class="memory-container">
      {#each memories as memory}
        <MemoryItem image={memory.image} text={memory.text} />
      {/each}
    </div>
  </main>
  
  <style>
    .memory-page {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
      min-height: 100vh;
      background: rgba(255, 182, 193, 0.3);
    }
  
    .title {
      font-size: 2.5rem;
      font-weight: bold;
      color: #ff69b4;
      margin-bottom: 20px;
    }
  
    .memory-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 75%; /* Match Content.svelte */
  max-width: 1100px; /* Allow it to be wider */
}

  
    @media (max-width: 768px) {
      .title {
        font-size: 2rem;
      }
    }
  </style>
  