// --------------------------------------------------------------------------
// ✅ 학습 주제
// --------------------------------------------------------------------------
// - [x] JSX를 사용해 React 엘리먼트를 생성해 마크업을 구성하는 방법을 학습합니다.
// --------------------------------------------------------------------------

// import * as React from 'react'
import { createRoot } from 'react-dom/client'

// const buttonElement = (
//   <button type="button" className="button">
//     저장
//   </button>
// )

const navElement = (
  <nav>
    <h2 className="sr-only">페이지 탐색 메뉴</h2>
    <ul>
      <li>
        <a href="/products">상품 목록</a>
      </li>
      <li>
        <a href="/cart">장바구니</a>
      </li>
    </ul>
  </nav>
)

createRoot(document.getElementById('root')!).render(navElement)
