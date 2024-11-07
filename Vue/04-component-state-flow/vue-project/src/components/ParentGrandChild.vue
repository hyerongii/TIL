<template>
  <div>
    <p>{{ myMsg }}</p>
    <button @click="updateName">이름 변경</button>
  </div>
</template>

<script setup>
defineProps({
  myMsg:String,
})

//  이름 변경 요청하는 이벤트 발신

const emit = defineEmits(['updateName'])

const updateName = function () {
  emit('updateName')
}
</script>

<style scoped>

</style>