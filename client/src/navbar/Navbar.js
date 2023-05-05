import React from 'react'
import "./Navbar.css"
import { ImSearch } from 'react-icons/im';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';
import {FaUserCircle} from 'react-icons/fa';
import { useState } from 'react';
import { SidebarList } from './SidebarList';

const Navbar = () => {
  let navigate = useNavigate()

  const [sidebar , setSidebar] = useState(false);
  const showSidebar = () => setSidebar(!sidebar);

  return (
  <div>
    <div className='navbar'>
      <div className='nav-logo'>
        <Link to="logo/">LOGO</Link>
      </div>
      
      <div className='nav-search'>
        <button onClick={()=>{navigate("/search")}}><ImSearch/>Search your Bus</button></div>
      
      <div className='nav-profile'>
        <button onClick={()=>showSidebar()}>
        <FaUserCircle className='profile-logo'/>
        </button>
      </div>
    </div>
    <div className={sidebar ? 'Sidebar active' : 'Sidebar'}>
            <ul className="Sidebarlist">
                {
                    SidebarList.map((val,key)=>{
                        return (
                            <li 
                            key={key}
                            className="row" 
                            onClick={() => {window.location.pathname = val.link;
                            }} 
                            >
                                {val.title}
                            </li>
                        );
                    })
                }
            </ul>
        </div>
    </div>
  )
}

export default Navbar