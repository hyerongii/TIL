// --------------------------------------------------------------------------
// ✅ 학습 주제
// 🔗 참고: https://ko.react.dev/learn
// --------------------------------------------------------------------------
// React 엘리먼트와 컴포넌트에 대해 학습한 후 커밋, 푸시합니다.
// --------------------------------------------------------------------------
// - [ ] JSX 마크업 작성
//   - [x] HTML과 다른 점
//     - [x] 셀프 클로징 (명시적 닫기 요구, 예: <img />, <meta />, <base />, <area />, <br />, <hr />)
//     - [x] 카멜케이스 속성 이름 (className, htmlFor, tabIndex 등)
//     - [x] 케밥케이스 속성 이름 (aria-*, data-* 등)
//     - [x] 루트 엘리먼트는 하나, 여러 형제 엘리먼트를 내보낼 경우 React.Fragment 사용 (<></> 약식 표현 사용 가능)
//     - [x] HTML -> JSX 변환 확장 활용 (https://bit.ly/41LOddq)
//   - [x] 데이터 표시
//     - [x] 변수 및 함수 호출 또는 객체를 사용해 데이터를 마크업에 끼워넣기
//     - [x] 마크업 코드는 결국 JavaScript 구문이므로 속성에도 동일한 방법 사용
//   - [x] 스타일 추가
//     - [x] CSS 스타일 파일 연결
//     - [x] class 속성으로 스타일 설정
//     - [x] style 속성으로 스타일 설정
// --------------------------------------------------------------------------
import '@/styles/section/info.css'
import { createRoot } from 'react-dom/client'

const rank = 1
const price = 21219900
const sectionLabel = '해외 도서 분야 앱 1위. 무제한 혜택이 9,900원'

const convertPriceWithComma = (price: number) => {
  return price.toLocaleString()
}

const list = [
  {
    title: ['20만 권의', '다양한 콘텐츠'],
  },
]

const [firstTitle, secondTitle] = list[0].title

const infoSectionElement = (
  <section
    id="info"
    className="info-section"
    aria-label={sectionLabel}
    // data-react-id="kjvicskmd20ds"
  >
    <div className="section-inner">
      <h3 className="section-header">
        국내 도서 분야 앱 {rank}위
        <br />
        무제한 혜택이 {convertPriceWithComma(price)}원
      </h3>
      <ul className="info-content">
        <li className="info-list">
          <div className="info-title-box">
            <span className="title-blk">
              {firstTitle} <br />
              {secondTitle}
            </span>
            <span className="icon-blk">
              <svg
                width="24"
                height="21"
                viewBox="0 0 24 21"
                fill="none"
                className="small-ico"
              >
                <path
                  d="M12.0002 3.9007L10.057 2.45933C9.55567 2.08747 8.94805 1.88672 8.32388 1.88672H1.81836V17.3273H8.32388C8.94805 17.3273 9.55567 17.528 10.057 17.8999L12.0002 19.3413M12.0002 3.9007L13.9434 2.45933C14.4447 2.08747 15.0523 1.88672 15.6765 1.88672H22.182V17.3273H15.6765C15.0523 17.3273 14.4447 17.528 13.9434 17.8999L12.0002 19.3413M12.0002 3.9007V19.3413"
                  stroke="#242424"
                  strokeWidth="1.81818"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
              <svg
                width="32"
                height="27"
                viewBox="0 0 32 27"
                fill="none"
                className="big-ico"
              >
                <path
                  d="M16 4.26923L13.3281 2.28734C12.6388 1.77604 11.8033 1.5 10.9451 1.5H2V22.7308H10.9451C11.8033 22.7308 12.6388 23.0068 13.3281 23.5181L16 25.5M16 4.26923L18.6719 2.28734C19.3612 1.77604 20.1967 1.5 21.0549 1.5H30V22.7308H21.0549C20.1967 22.7308 19.3612 23.0068 18.6719 23.5181L16 25.5M16 4.26923V25.5"
                  stroke="#242424"
                  strokeWidth="2.5"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </span>
          </div>
          <div className="info-content-box">
            온 가족이 보는 ‘패밀리 라운지’ 부터 <br />
            판타지/로맨스 장르 ‘스토리’ 까지
          </div>
        </li>
        <li className="info-list">
          <div className="info-title-box">
            <span className="title-blk">
              즐거운 <br />
              독서생활
            </span>
            <span className="icon-blk">
              <svg
                width="20"
                height="22"
                viewBox="0 0 20 22"
                fill="none"
                className="small-ico"
              >
                <rect
                  x="1.00195"
                  y="2.61523"
                  width="17.9972"
                  height="18.5"
                  rx="1.3844"
                  stroke="#242424"
                  strokeWidth="1.7305"
                />
                <path
                  d="M1.00195 6.07617L18.9991 6.07617"
                  stroke="#242424"
                  strokeWidth="1.7305"
                />
                <path
                  d="M16.4043 0.884342C16.4043 0.406479 16.0169 0.0190938 15.5391 0.0190938C15.0612 0.0190938 14.6738 0.406479 14.6738 0.884342L16.4043 0.884342ZM16.4043 2.96094L16.4043 0.884342L14.6738 0.884342L14.6738 2.96094L16.4043 2.96094Z"
                  fill="#242424"
                />
                <path
                  d="M5.32814 0.884342C5.32814 0.406479 4.94075 0.0190938 4.46289 0.0190938C3.98503 0.0190938 3.59764 0.406479 3.59764 0.884342L5.32814 0.884342ZM5.32814 2.96094L5.32814 0.884342L3.59764 0.884342L3.59764 2.96094L5.32814 2.96094Z"
                  fill="#242424"
                />
                <path
                  d="M6.53711 12.9993L9.53664 15.7681L15.5357 10.2305"
                  stroke="#242424"
                  strokeWidth="1.7305"
                  strokeLinejoin="round"
                />
              </svg>
              <svg
                width="30"
                height="31"
                viewBox="0 0 30 31"
                fill="none"
                className="big-ico"
              >
                <rect
                  x="2.21289"
                  y="3.72852"
                  width="25.5738"
                  height="26"
                  rx="1.96721"
                  stroke="#242424"
                  strokeWidth="2.45902"
                />
                <path
                  d="M2.21289 8.64648L27.7867 8.64649"
                  stroke="#242424"
                  strokeWidth="2.45902"
                />
                <path
                  d="M24.0986 1.26988C24.0986 0.590845 23.5482 0.0403752 22.8691 0.0403752C22.1901 0.0403753 21.6396 0.590845 21.6396 1.26988L24.0986 1.26988ZM24.0986 4.2207L24.0986 1.26988L21.6396 1.26988L21.6396 4.2207L24.0986 4.2207Z"
                  fill="#242424"
                />
                <path
                  d="M8.36037 1.26988C8.36037 0.590845 7.8099 0.0403752 7.13086 0.0403752C6.45182 0.0403753 5.90135 0.590845 5.90135 1.26988L8.36037 1.26988ZM8.36037 4.2207L8.36037 1.26988L5.90135 1.26988L5.90135 4.2207L8.36037 4.2207Z"
                  fill="#242424"
                />
                <path
                  d="M10.082 18.4833L14.3443 22.4177L22.8689 14.5488"
                  stroke="#242424"
                  strokeWidth="2.45902"
                  strokeLinejoin="round"
                />
              </svg>
            </span>
          </div>
          <div className="info-content-box">
            누적 가입자 1위, 840만 회원 데이터로 <br />
            만들어진 독서 동기부여 챌린지
          </div>
        </li>
        <li className="info-list">
          <div className="info-title-box">
            <span className="title-blk">
              AI 스마트 키워드와 <br />
              완독지수
            </span>
            <span className="icon-blk">
              <svg
                width="22"
                height="18"
                viewBox="0 0 22 18"
                fill="none"
                className="small-ico"
              >
                <path
                  d="M9.74101 9.4644C9.7158 9.44843 9.70223 9.42537 9.69253 9.40054L9.16889 7.36772C9.13786 7.25243 8.95944 7.25243 8.92841 7.36772L8.40477 9.40054C8.39701 9.4236 8.37956 9.44843 8.35629 9.4644L7.27992 10.1917C7.21398 10.236 7.21398 10.3265 7.27992 10.3708L8.35629 11.0981C8.3815 11.1141 8.39507 11.1371 8.40477 11.162L8.92841 13.1948C8.95944 13.3101 9.13786 13.3101 9.16889 13.1948L9.69253 11.162C9.70029 11.1389 9.71774 11.1141 9.74101 11.0981L10.8174 10.3708C10.8833 10.3265 10.8833 10.236 10.8174 10.1917L9.74101 9.4644Z"
                  fill="#242424"
                ></path>
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  d="M8.32564 0.835938C7.91958 0.835938 7.55384 1.08148 7.40009 1.45731L0.974609 17.1641H3.13549L8.99699 2.83594H9.10883L14.9703 17.1641H17.1312L10.7057 1.4573C10.552 1.08148 10.1862 0.835938 9.78018 0.835938H8.32564ZM21.0272 17.1641H19.0272V0.926847H21.0272V17.1641Z"
                  fill="#242424"
                ></path>
              </svg>
              <svg
                width="30"
                height="25"
                viewBox="0 0 30 25"
                fill="none"
                className="big-ico"
              >
                <path
                  d="M13.3111 13.0638C13.2755 13.0398 13.2564 13.0052 13.2427 12.968L12.5045 9.91877C12.4607 9.74583 12.2091 9.74583 12.1654 9.91877L11.4271 12.968C11.4162 13.0026 11.3916 13.0398 11.3588 13.0638L9.84121 14.1547C9.74824 14.2212 9.74824 14.3569 9.84121 14.4234L11.3588 15.5143C11.3943 15.5383 11.4135 15.5729 11.4271 15.6101L12.1654 18.6594C12.2091 18.8323 12.4607 18.8323 12.5045 18.6594L13.2427 15.6101C13.2537 15.5755 13.2783 15.5383 13.3111 15.5143L14.8286 14.4234C14.9216 14.3569 14.9216 14.2212 14.8286 14.1547L13.3111 13.0638Z"
                  fill="#242424"
                ></path>
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  d="M11.3158 0.765625C10.7676 0.765625 10.2738 1.09711 10.0663 1.60447L0.837891 24.1628L1.01292 24.2344H3.72579L12.2221 3.46562H12.4602L20.9565 24.2344H23.6694L23.8444 24.1628L14.616 1.60447C14.4084 1.09711 13.9147 0.765625 13.3665 0.765625H11.3158ZM29.1637 24.2344H26.4637V0.833903H29.1637V24.2344Z"
                  fill="#242424"
                ></path>
              </svg>
            </span>
          </div>
          <div className="info-content-box">
            완독 예상 확률과 시간을 제공하고 <br />
            AI로 책의 핵심까지 빠르게
          </div>
        </li>
        <li className="info-list">
          <div className="info-title-box">
            <span className="title-blk">
              작가의 탄생 <br />
              밀리로드
            </span>
            <span className="icon-blk">
              <svg
                width="22"
                height="25"
                viewBox="0 0 22 25"
                fill="none"
                className="small-ico"
              >
                <div>
                  <path
                    d="M16.3276 2.5625H6.1109C5.80818 5.58967 3.68916 10.096 2.89453 12.0224L11.2193 23.7527L19.544 12.0224C18.5223 9.77497 16.6303 5.58967 16.3276 2.5625Z"
                    stroke="#242424"
                    strokeWidth="1.89198"
                    strokeLinejoin="round"
                  />
                  <path
                    d="M11.2168 22.391V12.5527"
                    stroke="#242424"
                    strokeWidth="1.89198"
                  />
                  <rect
                    x="9.32422"
                    y="10.1309"
                    width="3.78396"
                    height="3.78396"
                    rx="1.89198"
                    fill="#242424"
                  />
                  <svg
                    width={26}
                    height={33}
                    viewBox="0 0 26 33"
                    fill="none"
                    className="big-ico"
                  >
                    <path
                      d="M19.9973 1.98242H5.99725C5.58244 6.13057 2.67873 12.3057 1.58984 14.9454L12.9973 31.0195L24.4047 14.9454C23.0047 11.8657 20.4121 6.13057 19.9973 1.98242Z"
                      stroke="#242424"
                      strokeWidth="2.59259"
                      strokeLinejoin="round"
                    />
                    <path
                      d="M12.998 29.1514V15.6699"
                      stroke="#242424"
                      strokeWidth="2.59259"
                    />
                  </svg>
                </div>

                <rect
                  x="10.4062"
                  y="12.3516"
                  width="5.18518"
                  height="5.18518"
                  rx="2.59259"
                  fill="#242424"
                ></rect>
              </svg>
            </span>
          </div>
          <div className="info-content-box">
            누구나 작가가 되어 글을 쓰고 <br />
            내일의 베스트셀러를 만나는 곳
          </div>
        </li>
      </ul>
      <p className="notice-blk">
        <sup>*</sup>2023년 11월 Google Play &amp; App Store 국내 전자책 구독
        서비스 기준
        <br />
        <sup>*</sup>2024년 10월 기준, 전자책 구독 서비스 이용자 기준
      </p>
    </div>
  </section>
)

createRoot(document.getElementById('root') as HTMLDivElement).render(
  infoSectionElement,
)