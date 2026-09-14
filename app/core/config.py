from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    app_name: str = "Student Mini System"
    data_file: Path = Path("data/store.json")


settings = Settings()
