import { currencyKR } from '@/utils/convert-price-with-comma'

// 속성(props)은 수정(mutation)하면 안됨
// 속성은 읽기전용
type Props = Readonly<{
  message?: string
  rank?: number
  price?: number
  className?: string
}>

export default function SectionTitle({
  message,
  rank = 1,
  price = 9900,
  className = 'text-orange-950',
}: Props) {
  return (
    <h3 className="section-header">
      <span className={className}>
        국내 도서 분야 앱 {rank}위
        <br />
        무제한 혜택이 {currencyKR(price)}
        <span>{message}</span>
      </span>
    </h3>
  )
}
