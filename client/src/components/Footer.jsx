
import {FaYoutube, FaFacebook, FaTwitter, FaLinkedin, FaInstagram } from 'react-icons/fa';

const Footer = () => {

    return ( <>
    <div className="socials flex justify-around bg-blue-500" >
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