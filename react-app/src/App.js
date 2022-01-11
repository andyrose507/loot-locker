import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from "react-redux";

import CartProvider from "./context/CartProvider";
import NavBar from "./components/NavBar";
import ItemPage from "./components/items/ItemPage"
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import HomePage from "./components/HomePage"
import { authenticate } from "./store/session";
import Footer from "./components/Footer";

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <CartProvider>
        <NavBar />
        <Switch>
          <ProtectedRoute path="/users" exact={true}>
            <UsersList />
          </ProtectedRoute>
          <ProtectedRoute path="/users/:userId" exact={true}>
            <User />
          </ProtectedRoute>
          <Route path="/items/:itemId">
            <ItemPage />
          </Route>
          <Route path="/" exact={true}>
            <HomePage />
          </Route>
        </Switch>
        <Footer />
      </CartProvider>
    </BrowserRouter>
  );
}

export default App;
