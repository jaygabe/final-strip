import axios from 'axios'
import { useEffect } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';
import { GoogleOAuthProvider } from '@react-oauth/google';
import "./App.css";

// Authentication
import {setAuth} from './redux/authSlice'
import {RootState} from './redux/store'

import {NavBar} from "./components/NavBar";

// Config
import {CSRFToken} from "./hooks/CSRFToken";

//  Admin
import { Home } from "./pages/admin/Home";
import { About } from "./pages/admin/About";
import { Pricing } from "./pages/admin/Pricing";

//  Authentication
import {Login} from "./pages/auth/Login";
import {Register} from "./pages/auth/Register";
import { Forgot } from "./pages/auth/Forgot";
import { Reset } from "./pages/auth/Reset";

//  Journal
import { Journal } from "./pages/journal/Journal";
import { Tournaments } from "./pages/journal/Touraments";
import { Events } from "./pages/journal/Events";
import { Bouts } from "./pages/journal/Bouts";
import { BoutView } from "./pages/journal/BoutView";
import { Fencers } from "./pages/journal/Fencers";
import { FencerView } from "./pages/journal/FencerView";
import { Lessons } from "./pages/journal/Lessons";
import { LessonView } from "./pages/journal/LessonView";

//  Error
import { Error404 } from "./pages/error/Error404";
import { Test } from './pages/test';


//  possible organize links:  https://stackoverflow.com/questions/58144678/organizing-react-routes-into-separate-components

function App() {
  const dispatch = useDispatch()
  const auth = useSelector((state: RootState) => state.auth.value)

  // should be refactored to use isAuthenticated
  useEffect(() => {
      (async () => {
          try {
              const {data} = await axios.get('api/auth/user');
              dispatch(setAuth(true))
              console.log('authenticated as :', data.email)
          } catch (e) {
              dispatch(setAuth(false))
              console.log('not authenticated')
          }
      })()
  }, [auth])

  return (
    <GoogleOAuthProvider clientId="1005506084219-mjeqr310a2kvpgo750lvn995h92e5mbl.apps.googleusercontent.com">
    <BrowserRouter>
      <NavBar />
      <CSRFToken />
      
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
        <Route path={"/journal/tournaments/"} element={<Tournaments />} />
        <Route path={"/journal/events/:tournamentSlug"} element={<Events />} />
        <Route path={"/journal/bouts/:eventSlug"} element={<Bouts />} />
        <Route path={"/journal/bout/:slug"} element={<BoutView />} />
        <Route path={"/journal/fencers"} element={<Fencers />} />
        <Route path={"/journal/fencer/:slug"} element={<FencerView />} />
        <Route path={"/journal/lessons"} element={<Lessons />} />
        <Route path={"/journal/lesson/:slug"} element={<LessonView />} />
        

        {/*  Error  */}
        <Route path="/404" element={<Error404/>} />
        <Route path="*" element={<Navigate replace to="/404" />} />
        <Route path="test" element={<Test />} />

      </Routes>

    </BrowserRouter>
    </GoogleOAuthProvider>
  )
}

export default App;
