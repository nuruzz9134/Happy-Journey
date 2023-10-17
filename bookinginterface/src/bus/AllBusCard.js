import React from 'react'
import './Bus.css'
import { useNavigate } from 'react-router-dom'

const AllBusCard = ({bus}) => {

  let route = bus.route.split("_")
  let from = route[0]
  let to = route[1]

  

  return (
    <div>
        <div className='card-container'>
        <div className='left-container'>
            <p></p>
            <div><b>Bus Number </b><span> : </span>{bus.number}</div>
            <p></p>
            <div><b>from</b><span> : </span>{from}</div>
            <div><b>to</b><span> : </span>{to}</div>
            <div>{bus.day}</div>
            <div><b>start at</b> <span> : </span>{bus.time}</div>
            <div><b>available seats</b> <span> : </span>{bus.seats}</div>
            <div><b>ticket price</b><span> : </span>{bus.travel_fee}</div>
        </div>
<<<<<<< HEAD
=======
        <div className='right-container'>
     
        </div>
>>>>>>> 6e77fe80d5e4e6de116c3b49e9266fea373e1ce4
    </div>
    </div>
  )
}

export default AllBusCard