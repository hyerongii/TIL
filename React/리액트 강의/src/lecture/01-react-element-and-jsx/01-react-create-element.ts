// --------------------------------------------------------------------------
// ✅ 학습 주제
// --------------------------------------------------------------------------
// - [x] React API를 사용해 리액트 엘리먼트를 생성해 마크업을 구성하는 방법을 학습합니다.
// - [x] ReactDOM API를 사용해 리액트 엘리먼트 트리를 DOM에 렌더링하는 방법을 학습합니다.
// --------------------------------------------------------------------------

import * as React from 'react'
import * as ReactDOM from 'react-dom/client'

const buttonElement = React.createElement(
  'button',
  {
    type: 'button',
    className: 'button',
    // children: '저장',
  },
  '저장',
)

console.log(buttonElement)

const navElement = React.createElement(
  'nav',
  null,
  React.createElement('h2', { className: 'sr-only' }, '페이지 탐색 메뉴'),
  React.createElement(
    'ul',
    null,
    React.createElement(
      'li',
      null,
      React.createElement('a', { href: '/products' }, '상품 목록'),
    ),
    React.createElement(
      'li',
      null,
      React.createElement('a', { href: '/cart' }, '장바구니'),
    ),
  ),
)

const rootElement = document.getElementById('root')

if (rootElement) {
  const reactDomRoot = ReactDOM.createRoot(rootElement)
  reactDomRoot.render(navElement)
}
