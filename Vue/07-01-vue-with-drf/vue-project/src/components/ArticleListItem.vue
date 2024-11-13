<template>
  <div>
    <h5>{{ article.id }}</h5>
    <h5>{{ article.title }}</h5>
    <h5>{{ article.content }}</h5>
    <RouterLink 
      :to="{name : 'DetailView', params : {id:article.id}}"
    >
      Detail
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  article:Object
})
</script>
