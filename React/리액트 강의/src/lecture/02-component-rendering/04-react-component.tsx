// --------------------------------------------------------------------------
// ✅ 학습 주제
// 🔗 참고: https://ko.react.dev/learn
// --------------------------------------------------------------------------
// React 엘리먼트와 컴포넌트에 대해 학습한 후 커밋, 푸시합니다.
// --------------------------------------------------------------------------
// - [x] 컴포넌트 작성
//   - [x] 대문자로 시작하는 이름
//   - [x] 마크업 구성 & 반환 값 (JSX 엘리먼트 = 리액트 엘리먼트)
//   - [x] 내보내기 & 불러오기
//   - [x] 컴포넌트 사용 & 중첩
//   - [x] 컴포넌트 속성(props)
//     - [x] 속성 추가 / 읽기
//     - [x] 속성 기본값 지정
//     - [x] 속성 타입 지정 (TypeScript Interface 또는 type alias)
//     - [x] 속성은 읽기전용(readonly, 불변 객체)
//     - [x] 기본 슬롯 (default slot, `children`)
//     - [x] 이름이 부여된 슬롯(named slot)
//     - [x] render props 패턴
// --------------------------------------------------------------------------

import { createRoot } from 'react-dom/client'

import '@/styles/section/info.css'
import './03-jsx-markup.css'

import InfoSection from '@/components/info-section'
import SectionTitle from '@/components/section-title'
import SectionFootnote from '@/components/section-footnote'

function App() {
  return (
    <div>
      <InfoSection
        // render props pattern
        render={(passiveData: string) => <SectionTitle message={passiveData} />}
        titleElement={<SectionTitle />}
        footNoteElement={<SectionFootnote />}
      ></InfoSection>
    </div>
  )
}

export default App

createRoot(document.getElementById('root')!).render(<App />)
