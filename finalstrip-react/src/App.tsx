import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { GoogleOAuthProvider } from '@react-oauth/google';
import "./App.css";

import {NavBar} from "./components/NavBar";

//  Admin
import { Home } from "./components/pages/admin/Home";
import { About } from "./components/pages/admin/About";
import { Pricing } from "./components/pages/admin/Pricing";

//  Authentication
import {Login} from "./components/pages/auth/Login";
import {Register} from "./components/pages/auth/Register";
import { Forgot } from "./components/pages/auth/Forgot";
import { Reset } from "./components/pages/auth/Reset";

//  Journal
import { Bouts } from "./components/pages/journal/Bouts";
import { BoutView } from "./components/pages/journal/BoutView";
import { Events } from "./components/pages/journal/Events";
import { Fencers } from "./components/pages/journal/Fencers";
import { FencerView } from "./components/pages/journal/FencerView";
import { Journal } from "./components/pages/journal/Journal";
import { Lessons } from "./components/pages/journal/Lessons";
import { LessonView } from "./components/pages/journal/LessonView";
import { Tournaments } from "./components/pages/journal/Touraments";

//  Error
import { Error404 } from "./components/pages/error/Error404";


//  possible organize links:  https://stackoverflow.com/questions/58144678/organizing-react-routes-into-separate-components

function App() {
  return (
    <GoogleOAuthProvider clientId="1005506084219-mjeqr310a2kvpgo750lvn995h92e5mbl.apps.googleusercontent.com">
    <BrowserRouter>
      <NavBar />
      <Routes>

        {/*  Admin  */}
        <Route path={"/"} element={<Home />} />
        <Route path={"/about"} element={<About />} />
        <Route path={"/pricing"} element={<Pricing />} />

        {/*  Authentication  */}
        <Route path={"/login"} element={<Login />} />
        <Route path={"/register"} element={<Register />} />
        <Route path={"/forgot"} element={<Forgot />} />
        <Route path={"/reset/:token"} element={<Reset />} />

        {/* Journal */}
        <Route path={"/journal"} element={<Journal />} />
        <Route path={"/journal/bouts/:slug"} element={<Bouts />} />
        <Route path={"/journal/bout/:slug"} element={<BoutView />} />
        <Route path={"/journal/events/:slug"} element={<Events />} />
        <Route path={"/journal/fencers"} element={<Fencers />} />
        <Route path={"/journal/fencer/:slug"} element={<FencerView />} />
        <Route path={"/journal/lessons"} element={<Lessons />} />
        <Route path={"/journal/lesson/:slug"} element={<LessonView />} />
        <Route path={"/journal/tournaments/"} element={<Tournaments />} />

        {/*  Error  */}
        <Route path="/404" element={<Error404/>} />
        <Route path="*" element={<Navigate replace to="/404" />} />
      </Routes>
    </BrowserRouter>
    </GoogleOAuthProvider>
  )
}

export default App;
