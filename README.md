# Wolkenlose KI für zu Hause

Unterlagen zum Vortrag auf den Grazer Linuxtagen 2025

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
LT_POSTGRES_USERNAME=gemeinde
LT_POSTGRES_PASSWORD=insecure
LT_POSTGRES_DATABASE=gemeinde
LT_POSTGRES_PORT=5432
```

Die Docker-Container starten:

```bash
docker compose up --detach
```
Beim ersten Mal wird das einige Sekunden dauern, da Docker die erforderlichen Docker-Images lädt.

Vorab das zu verwendende Ollama KI-Modell laden. Dieser Schritt kann auch entfallen, dann wird das Modell erst dann geladen, sobald es zum ersten Mal gebraucht wird.

```bash
docker compose exec ollama ollama pull gemma3:4b
```

Dies kann einige Minuten dauern, abhängig von der Geschwindigkeit der Internet-Anbindung.

Für einen ersten, schnellen Test der KI:

```bash
docker compose exec ollama ollama run gemma3:4b "Welche Farbe hat der Himmel?"
```

Nach einigen Sekunden sollte eine Antwort erscheinen wie diese:

> Der Himmel ist blau. Das liegt an einem Phänomen namens Rayleigh-Streuung. Kurzum: Die kürzeren Wellenlängen des blauen Lichts werden
von den kleinen Molekülen in der Atmosphäre stärker gestreut als andere Farben. Deshalb sehen wir den Himmel meistens blau.



## Daten vorbereiten

Die erforderlichen PDF-Dateien laden:

```bash
uv run prepare/download_gemeindezeitungen.py
```

Dies wird einige Sekunden dauern.

Die PDF-Dateien nach Markdown wandeln:

```bash
uv run prepare/convert_gemeindezeitung_pdf_to_markdown.py
```

