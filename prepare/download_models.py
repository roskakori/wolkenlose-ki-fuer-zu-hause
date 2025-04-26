import logging
import requests
from common.settings import OLLAMA_EMBEDDING_MODEL, OLLAMA_MODEL, OLLAMA_URL

_log = logging.getLogger(__name__)

def download_ollama_model(model_name: str):
    _log.info("Downloading %s", model_name)
    response = requests.post(
        f"{OLLAMA_URL}/api/pull",
        json={
            "model": OLLAMA_MODEL,
            "stream": False,
        },
    )
    response.raise_for_status()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    for model_name in [OLLAMA_MODEL, OLLAMA_EMBEDDING_MODEL]:
        download_ollama_model(model_name)
    _log.info("Done")