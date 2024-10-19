from pathlib import Path
from typing import Final

ROOT_DIR: Final[Path] = Path(__file__).parent.parent
ENV_FILE: Final[Path] = ROOT_DIR / ".env"
