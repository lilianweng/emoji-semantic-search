import gzip
import os

import jsonlines
import numpy as np
import openai
from flask import Flask, jsonify, request
from flask_cors import CORS

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = "https://api.openai.com/v1"
EMBEDDING_MODEL = "text-embedding-ada-002"

SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
EMBED_FILE = os.path.join(SERVER_DIR, "emoji-embeddings.jsonl.gz")


class EmojiSearchApp:
    def __init__(self):
        self._emojis = None
        self._embeddings = None

    def _load_emoji_embeddings(self):
        if self._emojis is not None and self._embeddings is not None:
            return

        with gzip.GzipFile(fileobj=open(EMBED_FILE, "rb"), mode="rb") as fin:
            emoji_info = list(jsonlines.Reader(fin))

        print("Lazy loading embedding info ...")
        self._emojis = [(x["emoji"], x["message"]) for x in emoji_info]
        self._embeddings = [x["embed"] for x in emoji_info]
        assert self._emojis is not None and self._embeddings is not None

    @property
    def emojis(self):
        if self._emojis is None:
            self._load_emoji_embeddings()
        return self._emojis

    @property
    def embeddings(self):
        if self._embeddings is None:
            self._load_emoji_embeddings()
        return self._embeddings

    def get_openai_embedding(self, text: str) -> list[float]:
        result = openai.Embedding.create(input=text, model=EMBEDDING_MODEL)
        return result["data"][0]["embedding"]

    def get_top_relevant_emojis(self, query: str, k: int = 20) -> list[dict]:
        query_embed = self.get_openai_embedding(query)
        dotprod = np.matmul(self.embeddings, np.array(query_embed).T)
        m_dotprod = np.median(dotprod)
        ind = np.argpartition(dotprod, -k)[-k:]
        ind = ind[np.argsort(dotprod[ind])][::-1]
        result = [
            {
                "emoji": self.emojis[i][0],
                "message": self.emojis[i][1].capitalize(),
                "score": (dotprod[i] - m_dotprod) * 100,
            }
            for i in ind
        ]
        return result


app = Flask(__name__)
emoji_search_app = EmojiSearchApp()
CORS(app, support_credentials=True)

@app.route("/search", methods=["POST"])
def search():
    error = None
    result = []

    query = request.get_json().get("query")
    try:
        result = emoji_search_app.get_top_relevant_emojis(query, k=20)
    except Exception as err:
        error = str(err)
    return jsonify(error=error, result=result)

@app.route("/")
def index():
    return 'Hello World!'

app.run()

