import React from 'react';
import WhatIsHook from './hooks/Hook';
import UseStateExample from './hooks/UseStateExample';
import UseEffectExample from './hooks/UseEffectExample';
import UseContextExample from './hooks/UseContextExample';
import UseRefExample from './hooks/UseRefExample';

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <Hook />
      <hr />
      <UseStateExample />
      <hr />
      <UseEffectExample />
      <hr />
      <UseContextExample />
      <hr />
      <UseRefExample />
    </div>
  );
}

export default App;
