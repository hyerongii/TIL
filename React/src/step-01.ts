import {createElement as h} from 'react'
import * as ReactDOM from 'react-dom/client'

// [TypeScript] React.ReactElement
// JavaScript Library

//<elementType prop1="value1"></elementType>
//<button type="button" class="btn btn-primary"> 리액트 버전 확인</button>    - 그냥 버튼이라 타입지정함

// 버튼 만들기
const buttonElement = h('button', {
  type: 'button',
  className: 'button primary-button',
  children: '리액트 버전 확인'
})

const navElement = h(
  'nav',
  null,
  h('h2', { className: 'sr-only' }, '페이지 탐색 메뉴'),
  h(
    'ul',
    null,
    h(
      'li',
      null,
      h(
        'a',
        {
          href: '/products',
        },
        '상품 목록',
      ),
    ),
  ),
)

// DOM API
//document.getElementById('idName')
const rootElement = document.getElementById('root')

if (rootElement) {
  const reactDomRoot = ReactDOM.createRoot(rootElement)
  // 실제 페이지에 렌더링
  reactDomRoot.render(navElement)
}