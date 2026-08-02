import type { Config } from 'tailwindcss';
export default {content:['./index.html','./src/**/*.{ts,tsx}','./components/**/*.{ts,tsx}'],theme:{extend:{fontFamily:{mono:['var(--font-mono)'],sans:['var(--font-sans)']}}},plugins:[]} satisfies Config;
