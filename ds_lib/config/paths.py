from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent.parent
MAIN_DIR = PACKAGE_DIR.parent
RESOURCES_DIR = MAIN_DIR / "resources"
TEMP_DIR = MAIN_DIR / ".temp"

if not RESOURCES_DIR.is_dir():
    RESOURCES_DIR.mkdir()
if not TEMP_DIR.is_dir():
    TEMP_DIR.mkdir()
