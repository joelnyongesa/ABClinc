/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily:{
        'primary': ['Poppins'],
        'secondary': ['Nunito'],
        'tertiary':['Montserrat']
      },
      colors:{ 
        "color-primary": "#313234",
        "color-secondary":"#5447E5",
        "color-tertiary": "#F1F5FF",
        "color-white": "#FCFDFF"
        
      }
    },
  },
  plugins: [],
}