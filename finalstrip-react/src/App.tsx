import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { GoogleOAuthProvider } from '@react-oauth/google';
import "./App.css";
import {Login} from "./components/Login";
import {Register} from "./components/Register";
import {NavBar} from "./components/NavBar";
import { Home } from "./components/Home";
import { Forgot } from "./components/Forgot";
import { Reset } from "./components/Reset"


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
