import { useState } from 'react'
import SearchBar from './SearchBar.js'
import './App.css'
import logo from './logo.png'

function App() {
  const [currentResults, setCurrentResults] = useState([])
  const [browserValue, setBrowserValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [subject, setSubject] = useState('Criptografia') // Estado para el ramo seleccionado

  const handleBrowserChange = (event) => {
    setBrowserValue(event.target.value)
  }

  const handleSubjectChange = (event) => {
    setSubject(event.target.value)
  }

  const clicker = () => {
    fetchData(subject)
  }

  const fetchData = async (subject) => {
    setIsLoading(true)
    console.log(browserValue)
    try {
      setCurrentResults([])
      console.log('{"text": "'+subject+'"}')
      const response = await fetch(`${process.env.REACT_APP_API_URL}/api/v1/${subject}/browse/`,
        {
          method: 'POST',
          headers: {
            'Content-type': 'application/json'
          },
          body: '{"text": "'+browserValue+'"}'
        }
      )
      if (!response.ok) {
        setIsLoading(false)
        throw new Error(response)
      }
      const data = await response.json()
      const rows = []
      for (const result of data.results) {
        const row = {
          doc_name: result.doc_name,
          link_ref: result.link_ref,
          similarity_percentage: result.similarity_percentage
        }
        rows.push(row)
      }
      setCurrentResults(rows)
      setIsLoading(false)
    }
    catch (error) {
      setIsLoading(false)
      console.log(error)
    }
  }

  return (
    <div className="container">
      <h1>
        <img src={logo} alt="Logo" className="logo" />
        SoloEstudio
      </h1>
      <select value={subject} onChange={handleSubjectChange} className="full-width">
        <option value="Criptografia">Criptografia</option>
        <option value="IA">Inteligencia Artificial</option>
      </select>
      <SearchBar value={browserValue} handle={handleBrowserChange} className="full-width"></SearchBar>
      <br></br>
      <button className='button-35' onClick={clicker}>Buscar</button>
      <ul className='holi'>
        {
          isLoading ? <p>Buscando documentos...</p> : currentResults.map(result => (
            <li key={result.link_ref}>
              <a href={result.link_ref} target="_blank" rel="noopener noreferrer">{result.doc_name}</a> | {result.similarity_percentage}%
            </li>
          ))
        }
      </ul>
    </div>
  )
}

export default App
