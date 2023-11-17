import { useState } from 'react'

import HealthAndSafetyIcon from '@mui/icons-material/HealthAndSafety';

function App() {
  

  return (
    <div className='flex flex-row justify-around p-10 font-primary'>
      <div className='flex'>
          <HealthAndSafetyIcon className='text-blue-500 my-1'/>
          <h1 className='text-2xl font-semibold'>HealthCare</h1>
      </div>
     
      <ul className='flex w-1/2 justify-around p-2'>
        <li >Home</li>
        <li>About</li>
        <li>Our services</li>
        <li>Blog</li>
      </ul>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Appointment</button>
    </div>
  )
}

export default App
