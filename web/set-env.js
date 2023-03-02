import { writeFile } from 'fs';// Configure Angular `environment.ts` file path
import dotenv from 'dotenv';

dotenv.load();

const targetPath = './src/environments/environment.ts';// Load node modules

const envConfigFile = `export const environment = {
   production: '${process.env.PRODUCTION}',
   API: '${process.env.API_URL}'
};`;

writeFile(targetPath, envConfigFile, function (err) {
    if (err) {
        throw console.error(err);
    } else {
        console.log(`Angular environment.ts file generated correctly at ${targetPath} \n`);
    }
});