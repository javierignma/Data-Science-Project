import React from 'react'
import './App.css'

function SearchBar(props) {
  return (
    <div>
      <input
        className='full-width2'
        placeholder='Busca algo...'
        value={props.value}
        onChange={props.handle}
        required
        autoFocus
      >
      </input>
    </div>
  )
}

export default SearchBar
