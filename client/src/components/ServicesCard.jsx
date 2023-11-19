import { servicesList } from './ServicesList';

function ServicesCard() {   
  return (
    <div className='pb-8'> 
        <h1 className='ml-60 text-3xl font-bold'>
            <span className='border-b-2 pb-3 border-blue-500'> Our Services </span>
        </h1>
        <div className=' w-10/12 m-auto justify-evenly flex flex-row flex-wrap '>  
            {servicesList.map((services,idx)=>(
                <div key={idx} className=" border rounded-3xl max-w-sm my-8 bg-white overflow-hidden shadow-lg p-2">

                    <div className='text-4xl flex justify-center items-center text-slate-50 my-1'>
                        <p className='rounded-full overflow-hidden bg-blue-500 p-2'> {services.icon} </p>
                    </div>

                    <div className="px-6 py-4 ">
                        <div className="font-bold text-xl mb-2 text-center"> {services.title} </div>
                        <p className="text-gray-700 text-base text-center"> {services.content} </p>
                    </div>   

                </div> 
            ))}
        </div>
    </div>
  )
}

export default ServicesCard