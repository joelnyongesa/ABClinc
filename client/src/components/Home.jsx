import hero from "../assets/hero.svg"

function Home() {
  return (
    <div className="flex">
        <img src={hero} alt="ABC" className="w-1/2 m-auto" />
    </div>
  )
}

export default Home