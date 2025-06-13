module.exports = {
  purge: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './src/components/**/*.{js,ts,jsx,tsx}',
    './src/containers/**/*.{js,ts,jsx,tsx}',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    minHeight: {
      '60vh': '60vh',
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
