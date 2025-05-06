<script>
  export let date = "";
  export let mood = "";
  export let text = "";
  export let image = "";
  export let altText = "";
  export let audio = "";

  // Normalize mood values from form
  const moodMap = {
    "very happy 😍😁": "veryHappy",
    "happy ☺️": "happy",
    "neutral 😑😐": "neutral",
    "sad 😢": "sad",
    "very sad 😭": "verySad"
  };

  const moodColors = {
    veryHappy: "rgba(255, 238, 238, 0.6)",
    happy: "rgba(255, 248, 220, 0.4)",
    neutral: "rgba(240, 240, 240, 0.3)",
    sad: "rgba(220, 235, 255, 0.3)",
    verySad: "rgba(210, 210, 255, 0.3)",
    default: "rgba(255, 255, 255, 0.15)"
  };

  $: cleanMood = moodMap[mood.toLowerCase()] || "default";
  $: bgColor = moodColors[cleanMood] || moodColors.default;

  $: hasValidImage = image && image.startsWith("http");
  $: hasValidAudio = audio && audio.startsWith("http");
</script>

<div class="memory-container" style="background: {bgColor}">
  <!-- Date Badge -->
  <div class="date-badge">{date}</div>

  <!-- Content -->
  <div class="text-section">
    <p class="text">{text}</p>
  </div>

  <!-- Image Section -->
  {#if hasValidImage}
    <div class="image-frame">
      <img src="{image}" alt="{altText}" class="tilted-image" />
    </div>
  {/if}

  <!-- Audio Section -->
  {#if hasValidAudio}
    <div class="audio-container">
      <audio controls src="{audio}"></audio>
    </div>
  {/if}
</div>

<style>
  .memory-container {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
    width: 90%;
    max-width: 1100px;
    margin: 30px auto;
    padding: 20px;
    border-radius: 16px;
    backdrop-filter: blur(10px);
    animation: fadeIn 0.8s ease-out;
    transition: transform 0.3s ease-in-out;
  }

  @media (min-width: 768px) {
    .memory-container {
      flex-direction: row;
      justify-content: space-between;
    }
  }

  .date-badge {
    position: absolute;
    top: 10px;
    left: 14px;
    background-color: rgba(255, 255, 255, 0.7);
    color: #333;
    font-size: 0.85rem;
    font-weight: bold;
    padding: 4px 10px;
    border-radius: 10px;
  }

  .text-section {
    flex: 1;
    padding: 10px;
    animation: fadeInUp 1s ease-out;
  }

  .text {
    font-size: 1.3rem;
    font-weight: 500;
    color: #ff69b4;
  }

  .image-frame {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 220px;
    background: white;
    padding: 8px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    transform: rotate(-8deg);
    transition: transform 0.3s ease-in-out;
    animation: fadeInTilt 1s ease-out;
  }

  .image-frame:hover {
    transform: scale(1.05) rotate(-8deg);
  }

  .tilted-image {
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
    transform: rotate(0deg);
  }

  .audio-container {
    width: 100%;
    margin-top: 10px;
    animation: fadeInUp 1s ease-out;
  }

  audio {
    width: 100%;
    border-radius: 6px;
  }

  @media (max-width: 768px) {
    .memory-container {
      text-align: center;
    }

    .text {
      font-size: 1.1rem;
    }

    .image-frame {
      height: 190px;
    }
  }

  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: scale(0.95);
    }
    to {
      opacity: 1;
      transform: scale(1);
    }
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes fadeInTilt {
    from {
      opacity: 0;
      transform: scale(0.8) rotate(0deg);
    }
    to {
      opacity: 1;
      transform: scale(1) rotate(-8deg);
    }
  }
</style>
