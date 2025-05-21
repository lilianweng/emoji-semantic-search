# Emoji Semantic Search

## Screenshot

The app is currently running at [emojisearch.app](https://www.emojisearch.app/)

<img width="955" alt="image" src="https://user-images.githubusercontent.com/901179/154786556-6acec72d-6a6c-4242-9449-db84fddb8d97.png">


## Local test


```
python -m venv venv
source venv/bin/activate
pip install -r server/requirements.txt
```

Get your OpenAI API key at [https://openai.com/api/](https://openai.com/api/).

Build embedding index:
```bash
OPENAI_API_KEY={api_key} python server/data/build.py
```

Start backend:
```bash
export OPENAI_API_KEY={api_key}
export EMOJI_SERVER_PORT=7777 # not required, default port is 5000. Recommended for MacOS since port 5000 can cause issues when using AirPlay.

python server/app.py 
```

Start frontend
```bash
cd client
npm install  # Run once
REACT_APP_SERVER_ADDRESS="http://localhost:5000" npm start # change port accordingly if EMOJI_SERVER_PORT was used above
```