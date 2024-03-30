/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{html,js,ts,svelte}"],
  theme: {
    extend: {
            colors: {
                "background": "#ffffff",
                "foreground": "#323232",
                "destructive": "#dc2626",
                "muted-foreground": "#666666",
                "pale": "#e8e8e8",
                "dark": "#212121",
                "muted": "#d3d3d3",
            },
            boxShadow: ({ theme }) => ({
                square: `4px 4px ${theme("colors").foreground}`,
            }),
        },
  },
  plugins: [],
}

