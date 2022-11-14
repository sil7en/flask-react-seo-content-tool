# flask-react-seo-content-tool
An mvp of seo-content-tool created with flask (and selenium) for backend, and react for the frontend.

## Dependencies

This mvp relies on a combination of Flask (python) for backend and React.js (javascript) for frontend.
This mvp only works on Windows system.
This mvp needs Google Chrome's last version available to work.

## For backend install
requirements:
- Python

First, create a new backend folder. Inside create venv:
```
mkdir backend
cd backend
pip venv venv
```

Then, activate venv and install follow libraries:
```
pip install Flask
pip install selenium
pip install webdriver_manager
pip install nltk
pip install -U spacy
pip install unidecode
pip install undetected-chromedriver
```



## For front end install
requirements:
- npm (Node.js)

to create new project execute:
```
npx create-react-app seo-content-tool --template typescript
```

add this to package.json file:

```
{
  "proxy": "http://localhost:5000"
}
```

### Config tailwind
on cmd execute
```
npm install -D tailwindcss postcss autoprefixer 
npx tailwindcss init -p
```

on new file "tailwind.config.js" add this content
```
content: [
    './src/**/*.{js,jsx,ts,tsx}',
],
```

add Tailwind directives to "src/index.css" file:
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```