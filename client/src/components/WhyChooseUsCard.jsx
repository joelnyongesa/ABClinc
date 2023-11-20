import { CiHospital1 } from "react-icons/ci";


function WhyChooseUsCard({ icon, heading, content}) {
  return (
    <div className="flex flex-row bg-white rounded-lg mr-5 mb-10">
        <div className="w-1/8 px-3 p-0 flex items-center justify-center">
            <div className="bg-blue-500 p-2 rounded-lg">
                {icon}
            </div>
        </div>
        <div className="py-5">
            <div className="flex flex-col">
                <h1 className="text-sm font-bold">{ heading }</h1>
                <p>{ content }</p>
            </div>
        </div>
    </div>
  )
}

export default WhyChooseUsCard