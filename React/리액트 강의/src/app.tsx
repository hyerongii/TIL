import InfoSection from './components/info-section'
import SectionFootnote from './components/section-footnote'
import SectionTitle from './components/section-title'

function App() {
  return (
    <div>
      <InfoSection
        isSigned={true}
        titleElement={<SectionTitle />}
        footNoteElement={<SectionFootnote />}
      />
    </div>
  )
}

export default App
