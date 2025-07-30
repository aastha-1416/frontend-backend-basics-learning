import React, { useReducer, useEffect } from 'react';
import { cartReducer, initialState } from './cartReducer';

const products = [
  { id: 1, name: 'T-shirt', price: 400 },
  { id: 2, name: 'Jeans', price: 800 },
  { id: 3, name: 'Shoes', price: 1200 },
];

const CartApp = () => {
  const [state, dispatch] = useReducer(cartReducer, initialState);

  useEffect(() => {
    dispatch({ type: 'CALCULATE_TOTAL' });
  }, [state.cart]);

  const addToCart = (product) => {
    dispatch({ type: 'ADD_ITEM', payload: product });
  };

  const removeFromCart = (id) => {
    dispatch({ type: 'REMOVE_ITEM', payload: id });
  };

  const updateQuantity = (id, quantity) => {
    dispatch({
      type: 'UPDATE_QUANTITY',
      payload: { id, quantity: parseInt(quantity) },
    });
  };

  const clearCart = () => {
    dispatch({ type: 'CLEAR_CART' });
  };

  const styles = {
    container: {
      fontFamily: 'Arial',
      padding: '2rem',
      maxWidth: '800px',
      margin: '0 auto',
      backgroundColor: '#f4f4f4',
      borderRadius: '10px',
    },
    section: {
      marginBottom: '2rem',
    },
    productCard: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      backgroundColor: '#fff',
      padding: '1rem',
      borderRadius: '8px',
      marginBottom: '1rem',
      boxShadow: '0 0 5px rgba(0,0,0,0.1)',
    },
    cartItem: {
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      backgroundColor: '#fff',
      padding: '1rem',
      borderRadius: '8px',
      marginBottom: '1rem',
      boxShadow: '0 0 5px rgba(0,0,0,0.1)',
    },
    input: {
      width: '60px',
      marginLeft: '10px',
    },
    button: {
      padding: '5px 10px',
      marginLeft: '10px',
      backgroundColor: '#007bff',
      color: '#fff',
      border: 'none',
      borderRadius: '4px',
      cursor: 'pointer',
    },
    clearButton: {
      padding: '10px 15px',
      backgroundColor: '#dc3545',
      color: '#fff',
      border: 'none',
      borderRadius: '4px',
      cursor: 'pointer',
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.section}>
        <h2>🛍️ Products</h2>
        {products.map(product => (
          <div key={product.id} style={styles.productCard}>
            <span>{product.name} - ₹{product.price}</span>
            <button style={styles.button} onClick={() => addToCart(product)}>Add to Cart</button>
          </div>
        ))}
      </div>

      <div style={styles.section}>
        <h2>🛒 Cart</h2>
        {state.cart.length === 0 ? (
          <p>Your cart is empty.</p>
        ) : (
          <>
            {state.cart.map(item => (
              <div key={item.id} style={styles.cartItem}>
                <span>{item.name} (₹{item.price})</span>
                <span>
                  Qty:
                  <input
                    type="number"
                    min="1"
                    value={item.quantity}
                    onChange={(e) => updateQuantity(item.id, e.target.value)}
                    style={styles.input}
                  />
                  <button style={styles.button} onClick={() => removeFromCart(item.id)}>Remove</button>
                </span>
              </div>
            ))}
            <h3>Total: ₹{state.total}</h3>
            <button style={styles.clearButton} onClick={clearCart}>Clear Cart</button>
          </>
        )}
      </div>
    </div>
  );
};

export default CartApp;
