<script>
    import Navbar from "$lib/components/Navbar.svelte";
  </script>
  
  <Navbar />
  <slot />
  <style>
    html{
      user-select: none;
    }
    
    html, body {
  min-height: 100vh;
  height: auto;
  overflow-x: hidden; /* Prevent horizontal scroll issues */
}

  </style>