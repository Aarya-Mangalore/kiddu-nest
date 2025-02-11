<script>
    import { onMount } from "svelte";
    import CakeBackground from "$lib/components/EmojiBackground.svelte";
  
    let countdown = "";
    const birthday = new Date(new Date().getFullYear(), 1, 15, 0, 0, 0); // Set to October 12 (Month is 0-based)(year, month, day, hour, minute, second)
  
    function updateCountdown() {
      const now = new Date();
      let diff = birthday - now;
  
      if (diff <= 0) {
        countdown = "🎉 Happy Birthday Aarna! 🎉";
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
      setInterval(updateCountdown, 1000); // Update every second
    });
  </script>
  
  <style>
    .countdown-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      text-align: center;
    }
  
    h1 {
      font-size: 3rem;
      color: #ff69b4; /* Pink Theme */
    }
  
    .timer {
      font-size: 2rem;
      font-weight: bold;
      color: #00e6e6; /* Cyan text for contrast */
      background: rgba(255, 255, 255, 0.2);
      padding: 10px 20px;
      border-radius: 10px;
      backdrop-filter: blur(5px);
    }
  </style>
  <CakeBackground emoji='🎂' bgcolor='rgba(240, 230, 170, 0.75)' floatemoji="🎉"/>
  
  <div class="countdown-container">
    <h1>Countdown to Kidamma's Birthday 🎂</h1>
    <div class="timer">{countdown}</div>
  </div>
  