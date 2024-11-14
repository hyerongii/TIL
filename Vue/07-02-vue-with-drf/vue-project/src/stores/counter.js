import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      headers: {
        Authorization: `Token ${token.value}`
      },
      url: `${API_URL}/api/v1/articles/`
    })
      .then((res) => {
        // console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // 회원가입 요청 액션
  const signUp = function (payload) {
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    // 위와 같은 코드임
    const {username, password1, password2} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        // username: username,
        // password1: password1,
        // password2: password2,
        // 위와 같은 코드임
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        console.log('회원가입 성공')

        // 회원가입 성공 후 자동으로 로그인까지 진행하기
        const password = password1
        logIn({username, password})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const {username, password} = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data:{
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        // 로그인 성공하면 자동으로 메인페이지로 이동!
        router.push({ name: 'ArticleView' })
        // console.log(res.data)
        // console.log('로그인 성공')
      })
      .catch((err) => {
        console.log(err)
      })
  } 

  // 토큰 값으로 로그인 여부 확인
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    }
    else {
      return true
    }
  })

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
