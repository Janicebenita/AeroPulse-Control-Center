import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const projectRoot=dirname(fileURLToPath(import.meta.url));
export default defineConfig({root:projectRoot,plugins:[react()],resolve:{alias:{'@':resolve(projectRoot)}},optimizeDeps:{noDiscovery:true,exclude:['react','react-dom','framer-motion','lucide-react','papaparse']},build:{target:'es2022',sourcemap:false}});
