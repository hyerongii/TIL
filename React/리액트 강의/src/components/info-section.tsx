import ServiceEmpty from './service-empty'
import ServiceList from './service-list'

type Props = Readonly<{
  isSigned?: boolean
  render?: (passiveData: string) => React.ReactElement
  titleElement?: React.ReactElement
  footNoteElement?: React.ReactElement
  children?: React.ReactNode
}>

export default function InfoSection({
  isSigned,
  render,
  titleElement,
  footNoteElement,
  children,
}: Props) {
  const passiveData = 'hello render props pattern'

  // switch(condition) {
  //   case A:
  //   case Z:
  //     return jsxElement
  //   case B:
  //   case K:
  //     return jsxElement
  //   default:
  //     return jsxElement
  // }

  // if (isSigned) {
  //   return (
  //     <section id="info" className="info-section">
  //       <div className="section-inner">
  //         {render?.(passiveData as string)}
  //         {titleElement}
  //         <ServiceList />
  //         {footNoteElement}
  //         {children}
  //       </div>
  //     </section>
  //   )
  // }

  let renderElement = <ServiceEmpty />

  if (isSigned) {
    renderElement = <ServiceList />
  }

  return (
    <section id="info" className="info-section">
      <div className="section-inner">
        {render?.(passiveData as string)}
        {titleElement}
        {isSigned && <ServiceList />}
        {/* {isSigned ? <ServiceList /> : <ServiceEmpty />} */}
        {renderElement}
        {footNoteElement}
        {children}
      </div>
    </section>
  )
}
