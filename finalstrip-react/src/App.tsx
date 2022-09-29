import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { GoogleOAuthProvider } from '@react-oauth/google';
import "./App.css";

import {Login} from "./components/pages/auth/Login";
import {Register} from "./components/pages/auth/Register";
import {NavBar} from "./components/NavBar";
import { Home } from "./components/pages/admin/Home";
import { Forgot } from "./components/pages/auth/Forgot";
import { Reset } from "./components/pages/auth/Reset";


function App() {
  return (
    <GoogleOAuthProvider clientId="1005506084219-mjeqr310a2kvpgo750lvn995h92e5mbl.apps.googleusercontent.com">
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path={"/"} element={<Home />} />
        <Route path={"/login"} element={<Login />} />
        <Route path={"/register"} element={<Register />} />
        <Route path={"/forgot"} element={<Forgot />} />
        <Route path={"/reset/:token"} element={<Reset />} />
      </Routes>
    </BrowserRouter>
    </GoogleOAuthProvider>
  )
}

export default App;
