# Wolkenlose KI für zu Hause

Dieses Projekt enthält die Unterlagen zum [Vortrag auf den Grazer Linuxtagen 2025](https://media.ccc.de/v/glt25-588-wolkenlose-ki-fr-eigene-dokumente-zu-hause).

## Einrichtung

Um die Inhalte selbst ausführen zu können, sind folgende Schritte erforderlich_

Den Python-Packet-Manager [uv](https://docs.astral.sh/uv/) einrichten.

Docker einrichten. Entweder über [Docker CE](https://docs.docker.com/engine/install/) oder mittels [Docker Desktop](https://www.docker.com/products/docker-desktop/). Bei letzterem ist die Gratis-Variante völlig ausreichend.

Die Python-Umgebung aufsetzen:

```bash
uv sync --python 3.12
```

Die Einstellungen für die Datenbank sind über die optionale Datei `.env` steuerbar. Fehlt diese Datei, kommen Default-Einstellungen zur Anwendung:

```dotenv
LT_OLLAMA_PORT=11444
LT_OLLAMA_MODEL=gemma3:4b
LT_OLLAMA_EMBEDDING_MODEL=jina/jina-embeddings-v2-base-de
LT_POSTGRES_USERNAME=gemeinde
LT_POSTGRES_PASSWORD=insecure
LT_POSTGRES_DATABASE=gemeinde
LT_POSTGRES_PORT=5444
```

Die Docker-Container starten:

```bash
docker compose up --detach
```
Beim ersten Mal wird das einige Sekunden dauern, da Docker die erforderlichen Docker-Images lädt.

Um die erforderlichen Modelle für Ollama aus dem Internet zu beziehen:

```bash
uv run python prepare/download_models.py
```

Je nach Geschwindigkeit der Internetverbindung kann dies einige Minuten dauern.

Alternativ lassen sich Modelle auch direkt über Docker beziehen:

```bash
docker compose exec ollama ollama pull gemma3:4b
docker compose exec ollama ollama pull jina/jina-embeddings-v2-base-de
```

Für einen ersten, schnellen Test der KI:

```bash
docker compose exec ollama ollama run gemma3:4b "Welche Farbe hat der Himmel?"
```
Nach einigen Sekunden sollte eine Antwort erscheinen wie diese:

> Der Himmel ist blau. Das liegt an einem Phänomen namens Rayleigh-Streuung. Kurzum: Die kürzeren Wellenlängen des blauen Lichts werden
von den kleinen Molekülen in der Atmosphäre stärker gestreut als andere Farben. Deshalb sehen wir den Himmel meistens blau.

## Daten vorbereiten

Die erforderlichen PDF-Dateien aus dem Internet laden:

```bash
uv run python prepare/download_gemeindezeitungen.py
```

Dies wird einige Sekunden dauern.

Die PDF-Dateien nach Markdown wandeln:

```bash
uv run python prepare/convert_pdf_to_markdown.py
```

Dies wird einige Minuten dauern.

## Jupyter-Notebook ansehen

Wer sich das im Video gezeigte Notebook nur ansehen möchte, kann diese eim einfachsten über direkt über die [Darstellung in GitHub](https://github.com/roskakori/wolkenlose-ki-fuer-zu-hause/blob/main/wolkenlose-ki-fuer-zu-hause.ipynb) machen.

## Jupyter-Notebook starten

Um das im Video gezeigte Notebook zu starten, gibt es mehrere Möglichkeiten.

Zum einen läuft es im Web-Browser:

```bash
uv run jupyter notebook wolkenlose-ki-fuer-zu-hause.ipynb
```

Damit lassen sich Python-Zellen bearbeiten und ausführen. SQL-Zellen allerdings sind nur zur Anzeige. Möchte man die SQL-Befehle auch auf die Datenbank anwenden, kann dazu eine SQL-Anwendung wie [DBeaver Community](https://dbeaver.io/download/) verwendet werden.

Eine andere Möglichkeit ist [PyCharm](https://www.jetbrains.com/pycharm/). Damit sind auch SQL-Zellen bearbeitbar und ausführbar.
