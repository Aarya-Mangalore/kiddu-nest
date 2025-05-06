<script>
    import { goto } from '$app/navigation';
    import BookBg from '$lib/components/EmojiBackground.svelte';
  
    function handleAddEntry() {
      goto('/diary');
    }
  </script>
  
  <BookBg emoji="📚" bgcolor="rgba(240, 230, 170, 0.75)" floatemoji="📕" clickdisabled=true/>
  
  <div class="add-entry-page">
    <h1 class="title">📖 Add New Diary Entry</h1>
  
    <div class="form-container">
      <img src="/kidu/KiduHiding2.jpg" alt="Form Header" class="form-header" />
  
      <!-- Scrollable iframe container for smaller screens -->
      <div class="iframe-wrapper">
        <iframe
          src="https://docs.google.com/forms/d/e/1FAIpQLSdujHdAESgZLC1pfQLWFmdI2Fuzs255yJJFEm3CyO1OOsJG9w/viewform?embedded=true"
          frameborder="0"
          marginheight="0"
          marginwidth="0"
          allowfullscreen
          loading="lazy"
        >Loading…</iframe>
      </div>
    </div>
  
    <button class="add-entry-btn" on:click={handleAddEntry}>
      🔙 to Diary page
    </button>
  </div>
  
  <style>
    .add-entry-page {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 2rem;
      min-height: 100vh;
      z-index: 5;
    }
  
    .title {
      font-size: 2.5rem;
      font-weight: bold;
      color: #ff69b4;
      margin-bottom: 1.5rem;
      text-align: center;
    }
  
    .add-entry-btn {
      background: linear-gradient(135deg, #ff69b4, #ffc0cb);
      color: white;
      border: none;
      padding: 0.75rem 1.5rem;
      font-size: 1.1rem;
      border-radius: 9999px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      margin-bottom: 2rem;
      z-index: 10;
    }
  
    .add-entry-btn:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 14px rgba(0, 0, 0, 0.3);
    }
  
    .add-entry-btn:active {
      transform: scale(0.97);
    }
  
    .form-container {
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(12px);
      padding: 1.5rem;
      border-radius: 12px;
      width: 90%;
      max-width: 800px;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.2);
      overflow: hidden;
    }
  
    .form-header {
      width: 100%;
      max-width: 640px;
      border-radius: 12px 12px 0 0;
      margin-bottom: 1rem;
    }
  
    .iframe-wrapper {
      width: 100%;
      max-width: 640px;
      height: 1500px; /* default desktop height */
      overflow: hidden;
      z-index: 20;
    }
  
    .iframe-wrapper iframe {
      width: 100%;
      height: 100%;
      border: none;
      border-radius: 12px;
    }
  
    @media (max-width: 600px) {
      .title {
        font-size: 1.8rem;
      }
  
      .add-entry-btn {
        font-size: 1rem;
        padding: 0.5rem 1.25rem;
      }
  
      .form-container {
        padding: 1rem;
      }
  
      .form-header {
        max-width: 100%;
      }
  
      .iframe-wrapper {
        height: 2000px; /* taller form for phones */
      }
    }
  </style>
  