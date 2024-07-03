import React, { useState } from 'react';

const SearchComponent = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:3001/api/v1/Criptografia/browse', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: query }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setResults(data.results.slice(0, 10)); // Limit results to maximum 10 items
    } catch (error) {
      console.error('Error fetching data:', error);
      // Handle error state or show a message to the user
    } finally {
      setLoading(false);
    }

    //console.log(response)
  };

  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <button onClick={handleSearch} disabled={loading}>{loading ? 'Searching...' : 'Buscar'}</button>

      <ul>
        {results.map((result, index) => (
          <li key={index}>
            <a href={result.link_ref} target="_blank" rel="noopener noreferrer">{result.doc_name}</a>
            <span> - Similarity: {result.similarity_percentage}%</span>
          </li>
        ))}
      </ul>

      {results.length === 0 && !loading && (
        <p>No documents found related to this course.</p>
      )}

      {loading && (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default SearchComponent;
