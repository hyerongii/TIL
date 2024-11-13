import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])

  // 장고 포트 번호
  const API_URL = 'http://127.0.0.1:8000'

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      //  보내고자 하는 장고 url
      url: `${API_URL}/api/v1/articles/`,
    })
      //  응답 받으면 응답 출력
      .then((res) => {
        // console.log(res)
        // articles 배열을 장고가 준 데이터로 채움
        articles.value = res.data
      })
      //  에러나면 에러 출력 
      .catch((error) => {
        console.log(error)
      })
  }


  return { articles, API_URL, getArticles }
}, { persist: true })
