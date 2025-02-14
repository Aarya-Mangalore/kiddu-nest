<script>
    import Navbar from "$lib/components/Navbar.svelte";
  </script>
  
  <Navbar />
  <slot />
  <style>
    html{
      user-select: none;
    }
  </style>