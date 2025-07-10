import React, { useState, useEffect } from 'react';

function UseEffectExample() {
  const [data, setData] = useState(null);

  useEffect(() => {
    setTimeout(() => {
      setData("Hello from useEffect!");
    }, 1000);
  }, []);

  return (
    <div>
      <h2>useEffect Example</h2>
      <p>{data || "Loading..."}</p>
    </div>
  );
}

export default UseEffectExample;
