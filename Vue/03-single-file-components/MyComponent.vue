<template>
  <div class="greeting">
    {{ msg }}
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  const msg = ref('hello')
  // 리턴 따로 필요없음
</script>

<!-- scoped: 해당 template 영역만 style 적용하겠다는 선언 -->
<style scoped>
  .greeting {
    color:red;
  }
</style>