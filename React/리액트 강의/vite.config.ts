import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { fileURLToPath } from 'node:url'
// import { resolve } from 'path'

const viteConfig = defineConfig({
  base: '/',
  server: {
    port: 3000,
  },
  preview: {
    port: 3010,
  },
  css: {
    devSourcemap: true
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      // '@': resolve(__dirname, 'src'),
    },
  },
  plugins: [
    react({
      jsxRuntime: 'automatic'
    })
  ],
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          react: [
            'react',
            'react-dom',
            'react-router',
            'react-calendar',
            'react-icons',
            'react-error-boundary',
          ],
          ecosystem: ['swiper', 'zustand', 'dayjs'],
          mui: ['@mui/material', '@mui/x-date-pickers'],
          supabase: ['@supabase/supabase-js'],
        } 
      }
    }
  }
})

export default viteConfig
