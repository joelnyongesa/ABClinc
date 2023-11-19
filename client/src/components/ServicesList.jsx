import { GiMedicines,GiHypodermicTest,GiTestTubes,GiFrontTeeth } from "react-icons/gi";
import { FaHeartbeat } from "react-icons/fa";
import { MdMasks } from "react-icons/md";


export const servicesList=[
    {
        icon:<GiMedicines />,
        title: 'Intensive Care',
        content: 'ABC Clinic is dedicated to providing exceptional intensive care services. Our state-of-the-art facility is equipped with advanced technology and staffed by a team of highly skilled professionals committed to delivering compassionate and comprehensive care.'
    },
    {
        icon: <GiHypodermicTest/>,
        title:'Online Medicine',
        content: 'ABC Clinic is a trusted online healthcare platform dedicated to providing convenient and accessible medical services. Our platform leverages advanced technology to connect patients with licensed healthcare professionals and facilitate the seamless delivery of essential healthcare services'
    },
    {
        icon: <FaHeartbeat/>,
        title:'Health Check',
        content: 'ABC Clinic is your partner in proactive healthcare, offering comprehensive health check services to ensure your well-being. Our streamlined process and advanced diagnostics empower you to take charge of your health..'
    },
    {
        icon: <GiTestTubes/>,
        title:'Laboratory Tests',
        content: 'We are your trusted partner for accurate and timely laboratory testing. Our state-of-the-art facility and experienced team ensure reliable results, contributing to informed healthcare decisions.'
    },
    {
        icon: <GiFrontTeeth/>,
        title:'General Dentistry',
        content: 'We do provide comprehensive and compassionate dental care. Our experienced team and modern facility ensure that you and your family receive top-notch oral health services..'
    },
    {
        icon: <MdMasks/>,
        title:'Urgent Surgery',
        content: 'ABC is your partner in urgent surgical care, dedicated to providing swift and expert interventions. In emergencies, trust us for timely and compassionate surgical solutions.'
    }
]