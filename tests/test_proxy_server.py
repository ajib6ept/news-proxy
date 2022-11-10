from news_proxy.engine import modify_text
from pathlib import Path

TEST_DATA_DIR = Path(__file__).resolve().parent.joinpath("fixtures")

ORIGINAL_TEXT_PATH = Path(TEST_DATA_DIR).joinpath("original_text.txt")
MODIFY_TEXT_PATH = Path(TEST_DATA_DIR).joinpath("modify_text.txt")


def test_modify_text() -> None:
    original_text = Path(ORIGINAL_TEXT_PATH).read_text()
    modified_text = Path(MODIFY_TEXT_PATH).read_text()
    assert modified_text == modify_text(original_text)
