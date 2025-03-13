import React from 'react'
import ReactDOM from 'react-dom'
import { createRoot } from 'react-dom/client'

// JSX (JavaScript extension XML Like syntax)
const navElement = (
  <nav>
      <h2 className="sr-only">페이지 탐색 메뉴</h2>
      <ul>
        <li>
          <a href="/products">상품목록</a>
        </li>
        <li>
          <a href="/cart">장바구니</a>
        </li>
      </ul>
    </nav>
)

createRoot(document.getElementById('root')!).render(
  navElement
)
