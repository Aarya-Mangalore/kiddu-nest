<script>
  import { onMount } from "svelte";
</script>

<style>
  nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: rgba(255, 105, 180, 0.3); /* Translucent pink */
    backdrop-filter: blur(10px); /* Smooth glass effect */
    padding: 12px 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  .nav-links {
    display: flex;
    justify-content: space-between;
    width: 70%;
    max-width: 1000px;
  }

  a {
    color: white;
    text-decoration: none;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 12px;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease-in-out;
  }

  /* Neon Glow Hover Effect */
  a::before {
    content: "";
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300%;
    height: 300%;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.3) 0%, rgba(255, 255, 255, 0) 80%);
    transition: all 0.3s ease-in-out;
    transform: translate(-50%, -50%) scale(0);
  }

  a:hover::before {
    transform: translate(-50%, -50%) scale(1);
  }

  /* Hover Effect: Neon Glow + Text Color Change */
  a:hover {
    color: #eb1818; /* Changes text color to cyan */
    background: rgba(255, 255, 255, 0.15); /* Fixed the syntax */
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
  }

  /* Responsive Navbar for Smaller Screens */
  @media (max-width: 768px) {
    nav {
      padding: 10px;
    }
    
    .nav-links {
      width: 90%;
    }

    a {
      font-size: 1rem;
      padding: 8px 14px;
    }
  }

  @media (max-width: 480px) {
    .nav-links {
      flex-direction: column;
      align-items: center;
      gap: 10px;
      width: 100%;
    }
  }
</style>


<nav>
  <div class="nav-links">
    <a href="/">Home</a>
    <a href="/memories">Memories</a>
    <a href="/messenger">Messenger</a>
    <a href="/countdown">Countdown</a>
  </div>
</nav>
<br>
<br>
<br>