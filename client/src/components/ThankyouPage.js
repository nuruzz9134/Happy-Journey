import React, { useEffect } from 'react'
import { useLocation } from 'react-router-dom'
import { useNavigate } from 'react-router-dom'
import { useState,useCallback } from 'react'
import { useWebSocket, ReadyState } from 'react-use-websocket/dist/lib/use-websocket'
import axios from 'axios'
import { type } from '@testing-library/user-event/dist/type'

const ThankyouPage = () => {

  const location = useLocation()
  const  navigate = useNavigate()
  const userId = location.state
  console.log("/////////",userId)


  // const [socket, setSocket] = useState(null);
  // const [message, setMessage] = useState(null);



  const getSocketUrl = useCallback(() => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(`ws://127.0.0.1:8000/notifications/${userId}/`)
      }, 2000);
    });
  }, []);
  
  const { sendMessage, lastMessage, readyState, getWebSocket } = useWebSocket(
    getSocketUrl, {
      onOpen : () => console.log('opened'),
      shouldReconnect : (closeEvent) => true,
      onMessage : (event)=> {
        const data = JSON.parse(event.data)
        console.log("Parsed Data...",data)
      },
      onError : (error) => console.log('errors>>',error),
      onClose : () => console.log('connection closed'),
    }
  );


  return (
    <div>Your seat booked ..thank you</div>
  )
}

export default ThankyouPage