# Emoji Semantic Search

Get your OpenAI API key at [https://openai.com/api/](https://openai.com/api/).

## Local test

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

## Screenshot

The app is currently running at [emojisearch.app](https://www.emojisearch.app/)

![image](https://user-images.githubusercontent.com/901179/152265271-bb447be2-37d2-4042-844a-99e656697a54.png)
