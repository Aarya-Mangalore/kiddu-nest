<script>
  import HeartBackground from "$lib/components/EmojiBackground.svelte";
</script>

<HeartBackground />

<main class="container">
  <!-- Left Section: Text -->
  <div class="text-section">
    <h1 class="title">Hello Kidammaa!!! 💖</h1>
    <p class="subtitle">
      Website ninnge maadidduu... issta aagutha annkondini... ☺️☺️
    </p>
  </div>

  <!-- Right Section: Tilted, Evenly Spaced & Animated Images -->
  <div class="image-gallery">
    <div class="image-frame img-1">
      <img src="/kidu/lakumi.jpg" alt="Memory 1" class="tilted-image">
    </div>
    <div class="image-frame img-2">
      <img src="/kidu/famCollage.jpg" alt="Memory 2" class="tilted-image">
    </div>
    <div class="image-frame img-3">
      <img src="/kidu/MeAndKidu.jpg" alt="Memory 3" class="tilted-image">
    </div>
    <div class="image-frame img-4">
      <img src="/kidu/happyKidu.jpg" alt="Memory 4" class="tilted-image">
    </div>
  </div>
</main>

<style>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 20px;
  }

  @media (min-width: 1024px) {
    .container {
      flex-direction: row;
      align-items: center;
      text-align: left;
    }
  }

  .text-section {
    flex: 1;
    text-align: center;
  }

  .title {
    font-size: 4rem;
    font-weight: 800;
    color: #ff69b4; /* Pink */
  }

  .subtitle {
    font-size: 1.5rem;
    color: #4a4a4a; /* Dark gray */
    max-width: 600px;
    margin-top: 1rem;
  }

  .image-gallery {
    flex: 1;
    display: flex;
    justify-content: space-evenly; /* ✅ Evenly Spaced */
    align-items: center;
    gap: 20px;
    margin-top: 20px;
  }

  .image-frame {
    background: white;
    padding: 8px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease-in-out;
    animation: fadeIn 1s ease-out, tiltAnimation 1s ease-in-out;
  }

  /* Tilt Animation on Load */
  @keyframes tiltAnimation {
    0% {
      transform: scale(0.8) rotate(0deg);
      opacity: 0;
    }
    100% {
      transform: scale(1) rotate(var(--tilt-angle));
      opacity: 1;
    }
  }

  /* Subtle Fade-In Effect */
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  /* Assigning Different Tilt Angles */
  .img-1 { --tilt-angle: -8deg; transform: rotate(-8deg); }
  .img-2 { --tilt-angle: 5deg; transform: rotate(5deg); }
  .img-3 { --tilt-angle: -6deg; transform: rotate(-6deg); }
  .img-4 { --tilt-angle: 8deg; transform: rotate(8deg); }

  /* Hover Effect (Keeps Tilt) */
  .image-frame:hover {
    transform: scale(1.1) rotate(var(--tilt-angle)); /* ✅ Keeps tilt */
  }

  .tilted-image {
    width: 140px;
    height: 180px;
    object-fit: cover;
    border-radius: 8px;
  }
</style>
