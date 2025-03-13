import { defineConfig } from "vite"

const viteConfig = defineConfig({
  base: '/',
  // 개발용 서버
  server: {
    port:3000,
  },
  // preview server
  preview: {
    port:3010,
  }
})

export default viteConfig