import json
from pathlib import Path
from typing import Dict


class WorkerDataStore:
    def __init__(self, data_file: str = "worker_data.json"):
        self.data_file = Path(data_file)
        self.data_file.write_text('{}') if not self.data_file.exists() else None

    def load(self) -> Dict:
        return json.loads(self.data_file.read_text())

    def save(self, data: Dict) -> None:
        self.data_file.write_text(json.dumps(data, indent=4))
