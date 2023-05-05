import React from 'react'
import { Route,Routes } from "react-router-dom";
import Navbar from './navbar/Navbar';

import Home from './home/Home';
import Search from './search/Search';
import SearchBus from './components/SearchBus';
import BusSeats from './components/BusSeats';
import ConfirmBooking from './components/ConfirmBooking';
import ThankyouPage from './components/ThankyouPage';

import RegistrationForm from './auth/RegistrationForm';
import Login from './auth/Login';
import VerifyOTP from './auth/VerifyOTP';
import Logout from './auth/Logout';
import { useSelector } from 'react-redux';
import { acc_Token } from './features/AuthSlice';


const App = () => {
  const acess_Token = useSelector(acc_Token)
  return (
    <div>
      <header>{<Navbar/>}</header>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="search/" element={<Search/>}/>
        <Route path="searchedBus/" element={ acess_Token ? <SearchBus/> : <Login/>}/>
        <Route path="bookyourSeats/" element={<BusSeats/>}/>
        <Route path="confirmbooking/" element={<ConfirmBooking/>}/>
        <Route path="thankUpage/" element={<ThankyouPage/>}/>

        <Route path="registration/" element={<RegistrationForm/>}/>
        <Route path="login/" element={<Login/>}/>
        <Route path="verifyOTP/" element={<VerifyOTP/>}/>
        <Route path="logout/" element={<Logout/>}/>
      </Routes>
    </div>
  )
}

export default App
