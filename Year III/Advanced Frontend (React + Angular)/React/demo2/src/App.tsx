import React from 'react';

//react routes
import {
  Routes,
  Route,
  Link
} from "react-router-dom";

//components
import Input from './components/Input';
import Nav from './layouts/Nav';
import LoginForm from './modules/LoginForm';
import GetStartedPage from './pages/GetStarted';
import WelcomePage from './pages/Welcome';

function App() {
  return (
    <React.Fragment>
      <Nav/>
      <Routes>
        <Route path="/get-started" element={<GetStartedPage/>}></Route>
        <Route path="/welcome" element={<WelcomePage/>}></Route>
        <Route path="/" element={<WelcomePage/>}></Route>
      </Routes>
    </React.Fragment>
  )
}

export default App;
