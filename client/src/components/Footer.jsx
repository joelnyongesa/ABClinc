
import {FaYoutube, FaFacebook, FaTwitter, FaLinkedin, FaInstagram } from 'react-icons/fa';
import HealthAndSafetyIcon from '@mui/icons-material/HealthAndSafety';

const Footer = () => {

    return ( <>

<div className='footer flex flex-wrap flex-row justify-evenly p-10'>
    <div className='address mt-3'>
        <div className='flex'>
            <HealthAndSafetyIcon className='text-blue-500 my-1'/>
            <h1 className='text-2xl  text-indigo-800 mb-1'>ABCLINIC</h1>
        </div>
        <ul className='flex flex-col mr-4'>
            <li>1234 Nairobi</li>
            <li>Ngong Lane</li>
            <li>Phone: 0712 293878</li>
            <li>Contact: info@abc.com</li>
        </ul>
    </div>  
    <div className='about mt-3'>
         <h1 className='text-2xl text-indigo-800 mb-1'>About Us</h1>
        <ul className='flex flex-col mr-4'>
            <li>Our Mission & Values</li>
            <li>Transformation</li>
            <li>Diversity is our Speciality</li>
            <li>Publicationc & Reports</li>
        </ul>
    </div>
    <div className='about mt-3'>
            <h1 className='text-2xl text-indigo-800 mb-1'>Our Services</h1>
        <ul className='flex flex-col mr-4'>
            <li>Lung Diseases</li>
            <li>Orthopaedic</li>
            <li>Phamarcy</li>
            <li>Dental Services</li>
        </ul>
    </div>
    <div className='time mt-3'>
        <h1 className='text-2xl text-indigo-800 mb-1'>Hospital Time    </h1>
        <div className='flex'>
            <ul className='flex flex-col mr-2 text-purple-800 ' >
                <li>Mon-Fri</li>
                <li>Saturday</li>
                <li>Sunday</li>
                <li>Holidays</li>
            </ul>
            <ul className='flex text-gray-800 flex-col'>
                <li>08:00-20:00</li>
                <li>09:00-18:00</li>
                <li>09:00-18:00</li>
                <li>09:00-18:00</li>
            </ul>
        </div>
    </div>
</div>
    <div className="socials flex flex-row justify-around bg-color-secondary px-10 py-4" >
         <div className=" text-base text-white font-bold w-1/2 mx-60">&copy; ABClinic 2023. All rights reserved.</div>
         <div className='flex items-center justify-evenly w-1/2 text-color-white text-3xl mr-60'>
            <FaYoutube />
            <FaFacebook />
            <FaTwitter />
            <FaLinkedin />
            <FaInstagram />
         </div>
    </div>
    </> );
}
 
export default Footer;