/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{js,jsx,ts,tsx,html,css}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#D30502',
          50: '#fd8c8b',
          100: '#FD6A67',
          200: '#FC4744',
          300: '#FC2421',
          400: '#F60602',
          500: '#D30502',
          600: '#B00402',
          700: '#8D0301',
          800: '#690201',
          900: '#460100',
        },
      },
    },
  },
  plugins: [],
};
