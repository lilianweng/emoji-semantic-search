# Emoji Semantic Search

## Screenshot

The app is currently running at [emojisearch.app](https://www.emojisearch.app/)

<img width="955" alt="image" src="https://user-images.githubusercontent.com/901179/154786556-6acec72d-6a6c-4242-9449-db84fddb8d97.png">


## Local test

Get your OpenAI API key at [https://openai.com/api/](https://openai.com/api/).

Build embedding index:
```bash
OPENAI_API_KEY={api_key} python server/data/build.py
```

Start backend:
```bash
OPENAI_API_KEY={api_key} python server/app.py
```

Start frontend
```bash
cd client
npm install  # Run once
REACT_APP_SERVER_ADDRESS="http://localhost:5000" npm start
```
