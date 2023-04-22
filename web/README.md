# Web Docs

This document contains information about the web application of Brazilian Worker.

## Deployment

### Local
* Environment Variables:
  - `API_URL`: http://localhost:5000/api/v1

### Staging (Preview)
* Environment Variables:
  - `API_URL`: https://braworstg-1-n2421623.deta.app/api/v1

### Production
* Environment Variables:
  - `API_URL`: https://braworprd-1-t9869704.deta.app/api/v1

* Settings:
  - build: node set-env.js && ng build --configuration production
  - output: dist (default)
  - install: npm install (default)
  - development: ng serve --port $PORT --prod

## Notes
- The `set-env.js` script is used to set the environment variables in the `environment.ts` file. This is necessary because the environment variables are not available in the build process by security reasons. Therefore, `set-env.js` script is executed before the build application using environment variables from web server.