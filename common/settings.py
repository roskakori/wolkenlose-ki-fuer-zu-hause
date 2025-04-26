import os
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv

load_dotenv()

_DEFAULT_OLLAMA_PORT = 11444
_DEFAULT_OLLAMA_MODEL = "gemma3:4b"
_DEFAULT_OLLAMA_EMBEDDING_MODEL = "jina/jina-embeddings-v2-base-de"
_DEFAULT_POSTGRES_DATABASE = "gemeinde"
_DEFAULT_POSTGRES_USERNAME = "gemeinde"
_DEFAULT_POSTGRES_PORT = 5444
_DEFAULT_POSTGRES_PASSWORD = "insecure"

DATA_FOLDER = Path(__file__).parent.parent / "data"

OLLAMA_MODEL = os.getenv("LT_OLLAMA_MODEL", _DEFAULT_OLLAMA_MODEL)
OLLAMA_EMBEDDING_MODEL = os.getenv("LT_OLLAMA_EMBEDDING_MODEL", _DEFAULT_OLLAMA_EMBEDDING_MODEL)
OLLAMA_PORT = int(os.getenv("LT_OLLAMA_PORT", str(_DEFAULT_OLLAMA_PORT)))
_DEFAULT_OLLAMA_URL = f"http://localhost:{OLLAMA_PORT}"
OLLAMA_URL = os.getenv("LT_OLLAMA_URL", _DEFAULT_OLLAMA_URL)

POSTGRES_DATABASE = os.getenv("LT_POSTGRES_DATABASE", _DEFAULT_POSTGRES_DATABASE)
POSTGRES_USERNAME = os.getenv("LT_POSTGRES_USERNAME", _DEFAULT_POSTGRES_USERNAME)
POSTGRES_PASSWORD = os.getenv("LT_POSTGRES_PASSWORD", _DEFAULT_POSTGRES_PASSWORD)
POSTGRES_PORT = int(os.getenv("LT_POSTGRES_PORT", str(_DEFAULT_POSTGRES_PORT)))
POSTGRES_HOST = "localhost"
POSTGRES_URI = (
    f"postgresql://{quote(POSTGRES_USERNAME)}:{quote(POSTGRES_PASSWORD)}@{quote(POSTGRES_HOST)}:"
    f"{POSTGRES_PORT}/{quote(POSTGRES_DATABASE)}"
)

# The minimum number of non-empty lines an article needs to be considered for the database.
MIN_ARTICLE_LINE_COUNT = 5
