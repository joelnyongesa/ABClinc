
import {FaYoutube, FaFacebook, FaTwitter, FaLinkedin, FaInstagram } from 'react-icons/fa';
import HealthAndSafetyIcon from '@mui/icons-material/HealthAndSafety';

const Footer = () => {

    return ( <>
<div className='bg-color-tertiary'>
<div className='footer flex mx-60 p-10'>
    <div className='address w-1/4'>
        <div className='flex'>
            <HealthAndSafetyIcon className='text-blue-500 my-1'/>
            <h1 className='text-2xl  text-indigo-800'>ABCLINIC</h1>
        </div>
        <ul className='flex flex-col mr-4'>
            <li>1234 Nairobi</li>
            <li>Ngong Lane</li>
            <li>Phone: 0712 293878</li>
            <li>Contact: info@abc.com</li>
        </ul>
    </div>  
    <div className='about w-1/4'>
         <h1 className='text-2xl text-indigo-800'>About Us</h1>
        <ul className='flex flex-col mr-4'>
            <li>Our Mission & Values</li>
            <li>Transformation</li>
            <li>Diversity is our Speciality</li>
            <li>Publicationc & Reports</li>
        </ul>
    </div>
    <div className='about w-1/4'>
            <h1 className='text-2xl text-indigo-800'>Our Services</h1>
        <ul className='flex flex-col mr-4'>
            <li>Lung Diseases</li>
            <li>Orthopaedic</li>
            <li>Phamarcy</li>
            <li>Dental Services</li>
        </ul>
    </div>
    <div className='time w-1/4'>
        <h1 className='text-2xl text-indigo-800'>Hospital Time    </h1>
        <div className='flex'>
            <ul className='flex flex-col mr-4 text-purple-800' >
                <li>Monday-Friday</li>
                <li>Saturday</li>
                <li>Sunday</li>
                <li>Holidays</li>
            </ul>
            <ul className='flex flex-col mr-4 text-gray-800'>
                <li>08:00-20:00</li>
                <li>09:00-18:00</li>
                <li>09:00-18:00</li>
                <li>09:00-18:00</li>
            </ul>
        </div>
    </div>
</div>
</div>
    <div className="socials flex justify-around bg-color-secondary px-10 py-2" >
         <div className="mt-4 text-base text-white font-bold">&copy; ABClinic 2023. All rights reserved.</div>
         <div className='flex items-center justify-around w-1/4'>
            <FaYoutube size={32} color='#FF0000' />
            <FaFacebook size={32} color='#3b5998'/>
            <FaTwitter size={32} color='##1D9BF0'/>
            <FaLinkedin size={32} color='#0077b5'/>
            <FaInstagram size={32} color='#e4405f'/>
         </div>
    </div>
    </> );
}
 
export default Footer;