"""
Download the Gemeindezeitung Edelschrott available from
<https://www.edelschrott.gv.at/buergerservice/gemeindezeitung/> in its
original PDF format.
"""
import logging

import requests

from common.settings import DATA_FOLDER

_BASE_URL_TEMPLATE = "https://www.edelschrott.gv.at/wp-content/uploads/{issue_name}.pdf"
_ISSUE_NAMES = [
    "1.VJ2022_web",
    "1.VJ2023_web",
    "1.VJ2024_web",
    "1.VJ2025_web",
    "1.VJ_2021_red",
    "1.VJ_2019",
    "1.VJ_2020",
    "2.VJ2022_web",
    "2.VJ2023_web",
    "2.VJ2024_web",
    "2.VJ_2019_web",
    "2.VJ_2020_web",
    "2.VJ_2021_web",
    "3.VJ2022_web",
    "3.VJ2023_web",
    "3.VJ2024web",
    "3.VJ_2020_web",
    "3.VJ_2021_red",
    "3.VJ_2019",
    "4.VJ-2023_web",
    "4.VJ2022_web",
    "4.VJ2024_web",
    "4.VJ_2020_web",
    "4.VJ_2021_web",
    "4.VJ_2019",
]
_HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:110.0) Gecko/20100101 Firefox/110.0"}
_log = logging.getLogger(__name__)

def download_all_gemeindezeitungen():
    for issue_name in _ISSUE_NAMES:
        download_gemeindezeitung(issue_name)

def download_gemeindezeitung(issue_name: str):
    issue_url = _BASE_URL_TEMPLATE.format(issue_name=issue_name)
    pdf_path = DATA_FOLDER / f"{issue_name}.pdf"
    if pdf_path.exists():
        _log.info("Skipping %s because it already exists", issue_name)
    else:
        _log.info("Downloading %s from %s", issue_name, issue_url)
        response = requests.get(issue_url, headers=_HEADERS)
        response.raise_for_status()
        with pdf_path.open("wb") as pdf_file:
            pdf_file.write(response.content)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    download_all_gemeindezeitungen()
    _log.info("Done")
