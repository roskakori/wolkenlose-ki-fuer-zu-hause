"""
Convert a PDF with a Gemeindezeitung to Markdown for further processing.
"""
import logging
from pathlib import Path
from marker.config.parser import ConfigParser
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

from common.settings import OLLAMA_URL, DATA_FOLDER

_config_parser = ConfigParser({
    "languages": "de",
    "llm_service": "marker.services.ollama.OllamaService",
    "ollama_base_url": OLLAMA_URL,
    "output_format": "markdown",
})

_log = logging.getLogger(__name__)

def convert_all_gemeindezeitungen_pdf_to_markdown():
    for pdf_path in DATA_FOLDER.glob("*.pdf"):
        convert_pdf_to_markdown(pdf_path)


def convert_pdf_to_markdown(path: Path):
    target_markdown_folder = DATA_FOLDER / path.stem
    readme_path = target_markdown_folder / "README.md"
    if readme_path.exists():
        _log.info("Skipping %s", path)
    else:
        _log.info("Converting %s to Markdown", path)
        target_markdown_folder.mkdir(exist_ok=True, parents=True)
        _log.info(
            "  Using config %s",
            _config_parser.generate_config_dict(),
        )
        converter = PdfConverter(
            config=_config_parser.generate_config_dict(),
            artifact_dict=create_model_dict(),
            processor_list=_config_parser.get_processors(),
            renderer=_config_parser.get_renderer(),
        )
        rendered = converter(str(path))
        text, _, images = text_from_rendered(rendered)
        _log.info("  Writing %s", readme_path)
        readme_path.write_text(text)
        for image_name, image in images.items():
            image_path = target_markdown_folder / image_name
            _log.info("  Writing %s", image_path)
            image.save(str(image_path))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    _log.info("Using Ollama at %s", OLLAMA_URL)
    convert_all_gemeindezeitungen_pdf_to_markdown()
    _log.info("Done")