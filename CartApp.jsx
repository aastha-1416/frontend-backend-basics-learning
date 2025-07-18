// CartApp.jsx

import React, { useReducer, useEffect } from "react";
import { cartReducer, initialState } from "./cartReducer";

const CartApp = () => {
  const [state, dispatch] = useReducer(cartReducer, initialState);

  const addItem = () => {
    const newItem = {
      id: Date.now(),
      name: "Item " + (state.cart.length + 1),
      price: Math.floor(Math.random() * 100 + 1),
    };
    dispatch({ type: "ADD_ITEM", payload: newItem });
  };

  const removeItem = (id) => {
    dispatch({ type: "REMOVE_ITEM", payload: { id } });
  };

  const updateQuantity = (id, quantity) => {
    dispatch({ type: "UPDATE_QUANTITY", payload: { id, quantity } });
  };

  const clearCart = () => {
    if (window.confirm("Are you sure you want to clear the cart?")) {
      dispatch({ type: "CLEAR_CART" });
    }
  };

  useEffect(() => {
    dispatch({ type: "CALCULATE_TOTAL" });
  }, [state.cart]);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2>🛒 Shopping Cart</h2>
      <button onClick={addItem}>Add Random Item</button>
      <button
        onClick={clearCart}
        disabled={!state.cart.length}
        style={{ marginLeft: "10px" }}
      >
        Clear Cart
      </button>

      <ul>
        {state.cart.map((item) => (
          <li key={item.id}>
            {item.name} - ₹{item.price} x{" "}
            <input
              type="number"
              value={item.quantity}
              min="1"
              onChange={(e) =>
                updateQuantity(item.id, parseInt(e.target.value, 10))
              }
              style={{ width: "50px" }}
            />{" "}
            <button onClick={() => removeItem(item.id)}>❌</button>
          </li>
        ))}
      </ul>

      <h3>Total: ₹{state.total.toFixed(2)}</h3>

      <pre>{JSON.stringify(state, null, 2)}</pre>
    </div>
  );
};

export default CartApp;
