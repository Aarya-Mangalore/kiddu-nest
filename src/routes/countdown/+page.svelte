<script>
  import { onMount } from "svelte";
  import CakeBackground from "$lib/components/EmojiBackground.svelte";

  let countdown = "";
  const birthday = new Date(new Date().getFullYear(), 1, 15, 0, 0, 0); // Feb 15

  function updateCountdown() {
    const now = new Date();
    let diff = birthday - now;

    if (diff <= 0) {
      countdown = "🎉 Happy Birthday Kidamma!! 🎉";
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);

    countdown = `${days}d ${hours}h ${minutes}m ${seconds}s`;
  }

  onMount(() => {
    updateCountdown();
    setInterval(updateCountdown, 1000);
  });
</script>

<CakeBackground
  emoji="🎂"
  bgcolor="rgba(240, 230, 170, 0.75)"
  floatemoji="🎉"
/>

<main class="container">
  <!-- Left Section: Countdown Timer -->
  <div class="text-section">
    <br />
    <h1 class="title">Countdown to Kidamma's Birthday 🎂</h1>
    <div class="timer">{countdown}</div>
  </div>

  <!-- Right Section: Tilted Image -->
  <div class="image-gallery">
    <div class="image-frame img-1">
      <img src="/kidu/Huva-Kidu.png" alt="Birthday Cake" class="tilted-image" />
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
    padding: 15px;
    text-align: center;
  }

  @media (min-width: 1024px) {
    .container {
      flex-direction: row;
      align-items: center;
      text-align: left;
      padding: 30px;
    }
  }

  .text-section {
    flex: 1;
    padding: 10px;
  }

  .title {
    font-size: 2.5rem;
    font-weight: 800;
    color: #ff69b4; /* Pink */
  }

  .timer {
    font-size: 1.8rem;
    font-weight: bold;
    color: #00e6e6; /* Cyan */
    background: rgba(255, 255, 255, 0.2);
    padding: 8px 12px;
    border-radius: 10px;
    backdrop-filter: blur(5px);
    width: fit-content;
    margin: auto;
  }

  .image-gallery {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px;
  }

  .image-frame {
    background: white;
    padding: 8px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease-in-out;
    animation:
      fadeIn 1s ease-out,
      tiltAnimation 1s ease-in-out;
  }

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

  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .img-1 {
    --tilt-angle: -8deg;
    transform: rotate(-8deg);
  }

  .image-frame:hover {
    transform: scale(1.1) rotate(var(--tilt-angle));
  }

  .tilted-image {
    width: 200px; /* ✅ Increased image size */
    height: 250px;
    object-fit: cover;
    border-radius: 8px;
  }

  /* Responsive Adjustments */
  @media (max-width: 768px) {
    .title {
      font-size: 2rem;
    }

    .timer {
      font-size: 1.4rem;
      padding: 6px 10px;
    }

    .tilted-image {
      width: 160px; /* ✅ Adjusted image for small screens */
      height: 200px;
    }

    .container {
      padding: 10px;
    }
  }

  @media (min-width: 1280px) {
    .tilted-image {
      width: 250px; /* ✅ Bigger image for larger screens */
      height: 300px;
    }
  }
</style>
