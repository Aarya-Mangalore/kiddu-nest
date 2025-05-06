<script>
  let isOpen = false;
  
</script>

<style>
  nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    background: rgba(255, 105, 180, 0.3); /* Translucent pink */
    backdrop-filter: blur(10px); /* Smooth glass effect */
    padding: 12px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
    overflow: hidden;
    
  }

  img{
    height: 50px;
  }

  .brand {
    display: flex;
    align-items: center;
    font-size: 2rem;
    font-weight: bold;
    color: white;
    margin-right: auto; /* Pushes links & toggle to the right */
    user-select: none;
  }

  .brand a{
    display: flex;
    align-items: center;
    font-size: 2rem;
    font-weight: bold;
    color: white;
    margin-right: auto; /* Pushes links & toggle to the right */
    user-select: none;
    padding: 0%;
  }

  .nav-links {
    display: flex;
    gap: 20px;
    padding-right: 20px; /* Prevents last link from getting cut off */
  }

  .menu-toggle {
    display: none;
    font-size: 2rem;
    cursor: pointer;
    color: white;
    padding-right: 45px; /* Prevents it from being cut off */
    position: absolute;
    right: 20px; /* Keeps it inside the viewport */
    z-index: 1100; /* Ensures it's above other elements */
  }

  /* Mobile Navigation */
  @media (max-width: 768px) {
    .nav-links {
      display: none;
      flex-direction: column;
      position: absolute;
      top: 60px;
      right: 20px;
      background: rgba(255, 105, 180, 0.8);
      backdrop-filter: blur(15px);
      padding: 10px;
      border-radius: 10px;
      box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
      padding-right: 30px;
      z-index: 1000;
    }

    .nav-links.open {
      display: flex;
      z-index: 1000;
    }

    .menu-toggle {
      display: block;
      z-index: 1000;
    }
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

  a:hover {
    color: #eb1818;
    background: rgba(255, 255, 255, 0.15);
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
  }
</style>

<nav>
  
  <div class="brand">
    <a href="/">
    <img alt="Logo" src="/favicon.ico">
    KidduNest</a></div>
  
  <div class="menu-toggle" on:click={() => (isOpen = !isOpen)}>☰</div>

  <div class="nav-links {isOpen ? 'open' : ''}">
    <a href="/">Home</a>
    <a href="/memories">Memories</a>
    <a href="/countdown">Birthday!!!</a>
    <a href="/diary">Diary</a>
  </div>
</nav>
<br>