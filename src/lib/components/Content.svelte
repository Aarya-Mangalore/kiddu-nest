<script>
    export let image = "";
    export let altText = "";
    export let text = "";
  </script>
  
  <div class="memory-container">
    <!-- Text Section -->
    <div class="text-section">
      <p class="text">{text}</p>
    </div>
  
    <!-- Image Section -->
    <div class="image-frame">
      <img src={image} alt={altText} class="tilted-image" />
    </div>
  </div>
  
  <style>
    .memory-container {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      width: 75%;
      max-width: 1100px;
      margin: auto;
      padding: 20px;
      background: rgba(255, 255, 255, 0.15);
      border-radius: 12px;
      backdrop-filter: blur(10px);
      transition: transform 0.3s ease-in-out;
    }
  
    @media (min-width: 768px) {
      .memory-container {
        flex-direction: row;
        text-align: left;
      }
    }
  
    @media (max-width: 767px) {
      .memory-container {
        flex-direction: column;
        text-align: center;
        width: 90%;
      }
    }
  
    .text-section {
      flex: 1;
      padding: 10px;
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
      width: 200px;
      height: 220px;
      background: white;
      padding: 8px;
      box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
      transition: transform 0.3s ease-in-out;
      animation: fadeIn 1s ease-out, tiltAnimation 1s ease-in-out;
      overflow: hidden;
      border-radius: 8px;
      transform: rotate(-8deg); /* Tilt the entire frame */
    }
  
    @keyframes tiltAnimation {
      0% {
        transform: scale(0.8) rotate(0deg);
        opacity: 0;
      }
      100% {
        transform: scale(1) rotate(-8deg);
        opacity: 1;
      }
    }
  
    .image-frame:hover {
      transform: scale(1.1) rotate(-8deg);
    }
  
    .tilted-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 8px;
      transform: rotate(0deg); /* Counteract the frame's rotation */
    }
  
    /* Responsive Adjustments */
    @media (max-width: 768px) {
      .text {
        font-size: 1.1rem;
      }
  
      .image-frame {
        width: 160px;
        height: 180px;
      }
    }
  </style>
  