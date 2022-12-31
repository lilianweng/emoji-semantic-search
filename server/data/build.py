import gzip
import json
import os
from typing import Dict, List

import emoji
import openai
import tqdm

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = "https://api.openai.com/v1"

SERVER_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
EMBEDDING_MODEL = "text-embedding-ada-002"

def get_embeddings(inp: List[str], batch: int=1000, inp_type: str="doc") -> List[List[float]]:
    i = 0
    outputs = []
    while i < len(inp):
        result = openai.Embedding.create(input=inp[i:i+batch], model=EMBEDDING_MODEL)
        outputs += [x["embedding"] for x in result['data']]
        i += batch
    assert len(outputs) == len(inp)
    return outputs


def write_jsonl(filename: str, data: List[Dict]):
    assert filename.endswith(".jsonl.gz")
    with open(filename, "wb") as fp:
        with gzip.GzipFile(fileobj=fp, mode="wb") as gz:
            for x in tqdm.tqdm(data):
                gz.write((json.dumps(x) + "\n").encode("utf-8"))


def extract_emoji_messages() -> Dict[str, str]:
	data = open(os.path.join(SERVER_DIR, "data/emoji-data.txt")).readlines()
	data = [x.split("\t") for x in data if not x.startswith("#")]
	emojis_msg = {
		x[-1].split("(")[1].split(")")[0]: x[-1].split("(")[1].split(")")[1].lower().strip() 
		for x in data
	}

	# Combine two sources of emoji messages
	emojis_dict = emoji.UNICODE_EMOJI["en"]
	emojis_full_msg = {}
	for k in emojis_dict:
	    msg = emojis_dict[k].strip(":").replace("_", " ").replace("-", " ").lower()
	    other_msg = emojis_msg.get(k)
	    if other_msg and len(other_msg) > len(msg):
	        msg = other_msg
	    emojis_full_msg[k] = msg

	# Dedupe the emojis.
	msg2emoji = {msg: [] for msg in emojis_full_msg.values()}
	for em, msg in emojis_full_msg.items():
	    msg2emoji[msg].append(em)
	emojis_full_msg_dedupe = {ems[-1]: msg for msg, ems in msg2emoji.items()}
	
	return emojis_full_msg_dedupe


def main():
	# Query embeddings
	emoji_messages = extract_emoji_messages()
	descriptions = [f"The emoji {em} is about {msg}." for em, msg in emoji_messages.items()]
	embeddings = get_embeddings(descriptions)

	# Save embeddings
	info = [
		{"emoji": em, "message": msg, "embed": embed} 
		for (em, msg), embed in zip(emoji_messages.items(), embeddings)
	]
	output_filename = os.path.join(SERVER_DIR, "emoji-embeddings.jsonl.gz")
	write_jsonl(output_filename, info)


if __name__ == "__main__":
	main()
