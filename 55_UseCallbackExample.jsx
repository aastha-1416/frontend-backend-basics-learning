import React, { useState, useCallback } from 'react';

const Child = React.memo(({ onClick }) => {
  console.log('Child rendered');
  return <button onClick={onClick}>Click Me</button>;
});

function UseCallbackExample() {
  const [count, setCount] = useState(0);

  const handleClick = useCallback(() => {
    setCount(prev => prev + 1);
  }, []);

  return (
    <div>
      <h2>Count: {count}</h2>
      <Child onClick={handleClick} />
    </div>
  );
}

export default UseCallbackExample;
