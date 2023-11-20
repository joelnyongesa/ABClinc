
function WhyChooseUsCard({ icon, heading, content}) {
    // Why choose us
  return (
    <div className="flex flex-row bg-white rounded-lg mx-10 my-5 w-3/4">
        <div className="w-1/8 px-6  flex items-center justify-center">
            <div className="bg-blue-500 rounded-lg">
                {icon}
            </div>
        </div>
        <div className="py-5">
            <div className="flex flex-col">
                <h1 className="text-2xl font-bold">{ heading }</h1>
                <p className="text-xl">{ content }</p>
            </div>
        </div>
    </div>
  )
}

export default WhyChooseUsCard