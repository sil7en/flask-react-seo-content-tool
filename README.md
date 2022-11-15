# flask-react-seo-content-tool
An mvp of seo-content-tool created with flask (and selenium) for backend, and react for the frontend.

## Dependencies

This mvp relies on a combination of Flask (python) for backend and React.js (javascript) for frontend.
This mvp only works on Windows system.
This mvp needs Google Chrome's last version available to work.

## For backend install
requirements:
- Python
- Google Chrome's last version

First, move to backend folder. Inside create a new venv:
```
cd backend
py -m venv venv
```

Then, activate venv on bash
```
source venv/Scripts/activate
```

with venv active install follow libraries:
```
pip install Flask
pip install flask-restful
pip install selenium
pip install webdriver_manager
pip install nltk
pip install -U spacy
pip install unidecode
pip install undetected-chromedriver
```



## For front end install
requirements:
- npm (Node.js) or yarn

### First time only:

to create new project move to frontend folder and then execute:
```
cd frontend
yarn create react-app . --template typescript
```

add this at bottom package.json file:

```
{
  ...
  "proxy": "http://localhost:5000"
}
```

### Config tailwind
on cmd go to frontend folder and execute
```
cd frontend
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