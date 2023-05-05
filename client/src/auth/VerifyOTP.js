import React from 'react'
import './Login.css'
import { useState } from 'react'
import AuthSlice from '../features/AuthSlice'
import { useLocation } from 'react-router-dom'
import {StoreToken,GetToken} from './LocalStore_Token'
import {useVerifyOTPMutation } from './UserAuthApi'
import { useDispatch,useSelector } from 'react-redux';
import { useEffect } from 'react';
import { setUserToken } from '../features/AuthSlice'
import { useNavigate } from 'react-router-dom'



const VerifyOTP = () => {

    const location = useLocation()
    const navigate = useNavigate()
    const dispatch = useDispatch()

    const [enteredOtp,SetenteredOtp] = useState('')
    const [verifyOtp,respondData] = useVerifyOTPMutation()
    const [server_error,setServer_error] = useState('')

    const otpMsg = location.state.msg

    const HandleOTPsubmit = async(e)=>{
      e.preventDefault()
      const data ={
        email:location.state.email,
        otp:enteredOtp
      }
      const res = await verifyOtp(data)
      if (res.error){
        setServer_error(res.error.data)
        console.log(res.error.data)
      }
      if (res.data){
        console.log(res.data)
        StoreToken(res.data.token)
        let { access_token } = GetToken()
        dispatch(setUserToken({access_token:access_token}))
        navigate('/searchedBus')
        
      }
    }
    // let { access_token } = GetToken()
    // useEffect(()=>{
    //     dispatch(setUserToken({access_token:access_token}))
    // },[access_token,dispatch])



  return (
    <div>
      <form  onSubmit={HandleOTPsubmit}>
			<div class="form_wrap">
      <p>{otpMsg ? <div >**** {otpMsg}</div> : null}</p>
				<div class="input_wrap">
					<label for="otp">OTP</label>
					<input type="text" id="otp" onChange={e=>SetenteredOtp(e.target.value)} value={enteredOtp} />
				</div>

				<div class="input_wrap">
					<input type="submit" value="send otp" class="submit_btn"/>
				</div>
			</div>
		</form>
    </div>
  )
}

export default VerifyOTP