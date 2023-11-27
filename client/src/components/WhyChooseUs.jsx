import doc from "../assets/why-choose-us.svg"
import WhyChooseUsCard from "./WhyChooseUsCard"
import { CiHospital1 } from "react-icons/ci";
import { CiStethoscope } from "react-icons/ci";

function WhyChooseUs() {
    // Why choose us
  return (
    <div className="p-30 my-10 flex flex-col">
        <h1 className="text-3xl font-bold mb-5">
            <span className="border-b-2 border-blue-500 p-2 ml-60">
            Why Choose Us
            </span>
        </h1>
        <div className="flex flex-row justify-between w-10/12 h-1/2 mx-auto ">
            <div className="w-1/2 py-10  flex flex-col flex-wrap justify-center items-center">
                <WhyChooseUsCard icon={<CiHospital1 className="text-6xl text-white"/>} heading={"Medical and Surgical"} content={"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, quod."} />

                <WhyChooseUsCard icon={<CiHospital1 className="text-6xl text-white"/>} heading={"Medical and Surgical"} content={"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, quod."} />

                <WhyChooseUsCard icon={<CiStethoscope className="text-6xl text-white"/>} heading={"Intensive Care"} content={"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, quod."} />

                <WhyChooseUsCard icon={<CiStethoscope className="text-6xl text-white"/>} heading={"Intensive Care"} content={"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, quod."} />

            </div>

            <div className="w-1/2 flex">
                <img src={doc} alt="101 reasons to choose us" className="" />
            </div>
        </div>
    </div>
  )
}

export default WhyChooseUs