import React, { useState, useMemo } from 'react';

function UseMemoExample() {
  const [num, setNum] = useState(1);
  const [darkMode, setDarkMode] = useState(false);

  const factorial = useMemo(() => {
    console.log('Calculating...');
    return num <= 0 ? 1 : num * factorialOf(num - 1);
  }, [num]);

  const factorialOf = (n) => {
    return n <= 0 ? 1 : n * factorialOf(n - 1);
  };

  const theme = {
    backgroundColor: darkMode ? '#333' : '#fff',
    color: darkMode ? '#fff' : '#000',
    padding: '10px'
  };

  return (
    <div style={theme}>
      <input type="number" value={num} onChange={e => setNum(+e.target.value)} />
      <button onClick={() => setDarkMode(!darkMode)}>Toggle Theme</button>
      <p>Factorial: {factorial}</p>
    </div>
  );
}

export default UseMemoExample;
