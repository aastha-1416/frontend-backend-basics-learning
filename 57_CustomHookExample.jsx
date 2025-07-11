import React from 'react';
import useWindowWidth from './useWindowWidth';

function CustomHookExample() {
  const width = useWindowWidth();

  return <h2>Window width: {width}px</h2>;
}

export default CustomHookExample;
