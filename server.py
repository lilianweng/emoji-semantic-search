import os
import fire
from flask import Flask, jsonify, request
import gzip
import emoji
import openai
import time
import jsonlines
import numpy as np
from typing import Dict, List, Tuple
from flask_cors import CORS, cross_origin

openai.api_key = os.environ["OPENAI_API_KEY_PROD"]
openai.api_base = "https://api.openai.com"

with gzip.GzipFile(fileobj=open("emoji-embeddings.jsonl.gz", "rb"), mode="rb") as fin:
    emoji_info = list(jsonlines.Reader(fin))
emojis = [(x["emoji"], x["message"]) for x in emoji_info]
embeddings = [x["embed"] for x in emoji_info]


def get_embedding(text: str) -> List[float]:
    result = openai.Engine(f"text-similarity-curie-001").embeddings(input=text)
    return result["data"][0]["embedding"]


def get_top_relevant_emojis(query: str, k: int = 10) -> List[Tuple[str, str, float]]:
    query_embed = get_embedding(query)
    dotprod = np.matmul(embeddings, np.array(query_embed).T)
    m_dotprod = np.median(dotprod)
    ind = np.argpartition(dotprod, -k)[-k:]
    ind = ind[np.argsort(dotprod[ind])][::-1]
    result = [
        (emojis[i][0], emojis[i][1].capitalize(), (dotprod[i] - m_dotprod) * 100) for i in ind
    ]
    return result


def main(port: int = 12358, debug: bool = False):
    app = Flask(__name__)
    CORS(app, support_credentials=True)

    @app.route("/search", methods=["GET", "POST"])
    def search():
        error = None
        result = []

        query = request.get_json().get("query")
        try:
            result = get_top_relevant_emojis(query)
        except Error as err:
            error = str(err)
        return jsonify(error=error, result=result)

    app.run(port=port, debug=debug)


if __name__ == "__main__":
    fire.Fire(main)
