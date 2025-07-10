import React, { useState } from 'react';

function UseStateExample() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>useState Example</h2>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  );
}

export default UseStateExample;
