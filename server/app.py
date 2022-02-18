import gzip
import os
from typing import List, Tuple

import jsonlines
import numpy as np
import openai
from flask import Flask, jsonify, request
from flask_cors import CORS

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = "https://api.openai.com/v1"

SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
EMBED_FILE = os.path.join(SERVER_DIR, "emoji-embeddings.jsonl.gz")

with gzip.GzipFile(fileobj=open(EMBED_FILE, "rb"), mode="rb") as fin:
    emoji_info = list(jsonlines.Reader(fin))

emojis = [(x["emoji"], x["message"]) for x in emoji_info]
embeddings = [x["embed"] for x in emoji_info]


def get_embedding(text: str) -> List[float]:
    result = openai.Engine(f"text-similarity-babbage-001").embeddings(input=text)
    return result["data"][0]["embedding"]


def get_top_relevant_emojis(query: str, k: int = 20) -> List[Tuple[str, str, float]]:
    query_embed = get_embedding(query)
    dotprod = np.matmul(embeddings, np.array(query_embed).T)
    m_dotprod = np.median(dotprod)
    ind = np.argpartition(dotprod, -k)[-k:]
    ind = ind[np.argsort(dotprod[ind])][::-1]
    result = [
        {
            "emoji": emojis[i][0],
            "message": emojis[i][1].capitalize(),
            "score": (dotprod[i] - m_dotprod) * 100,
        }
        for i in ind
    ]
    return result


app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/search", methods=["POST"])
def search():
    error = None
    result = []

    query = request.get_json().get("query")
    try:
        result = get_top_relevant_emojis(query)
    except Exception as err:
        error = str(err)
    return jsonify(error=error, result=result)

app.run()

