import doc from "../assets/why-choose-us.svg"
import WhyChooseUsCard from "./WhyChooseUsCard"
import { CiHospital1 } from "react-icons/ci";
import { CiStethoscope } from "react-icons/ci";

function WhyChooseUs() {
  return (
    <div className="my-20 flex flex-col">
        <h1 className="text-3xl font-bold mb-5">
            <span className="border-b-2 border-blue-500 p-2">
            Why Choose Us
            </span>
        </h1>
        <div className="flex flex-row justify-between">
            <div className="w-1/2 py-10 border-4 flex flex-col flex-wrap">
                <WhyChooseUsCard icon={<CiHospital1 className="text-3xl text-white"/>} heading={"Medical and Surgical"} content={"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, quod."} />

                <WhyChooseUsCard icon={<CiStethoscope className="text-3xl text-white"/>} heading={"Intensive Care"} content={"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, quod."} />

                <WhyChooseUsCard icon={<CiStethoscope className="text-3xl text-white"/>} heading={"Intensive Care"} content={"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Optio, quod."} />

            </div>

            <div className="h-full w-1/2 flex flex-col items-center border-4">
                <img src={doc} alt="101 reasons to choose us" />
            </div>
        </div>
    </div>
  )
}

export default WhyChooseUs