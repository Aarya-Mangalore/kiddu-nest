import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: '0.0.0.0', // Expose to the network
		port: 5173, // Default Vite port
		strictPort: true // Ensures it doesn't switch to a different port
	}
});
