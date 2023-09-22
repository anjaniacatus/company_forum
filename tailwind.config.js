/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/templates/**/*.{html,js}"],

  theme: {
    extend: {},
  },

  plugins: [
    require("@tailwindcss/typography"),
    require("daisyui"),
    require("@tailwindcss/forms"),
  ],
  daisyui: {
      themes: ["light"],
       styled: true,
    base: true,
    utils: true,
    logs: true,
    rtl: false,
  },
}

