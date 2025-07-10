import React, { createContext, useContext } from 'react';

const UserContext = createContext();

function UseContextExample() {
  return (
    <UserContext.Provider value="Aastha Jani">
      <ChildComponent />
    </UserContext.Provider>
  );
}

function ChildComponent() {
  const name = useContext(UserContext);
  return <p>Hello, {name}</p>;
}

export default UseContextExample;
