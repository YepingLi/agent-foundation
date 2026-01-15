from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class EvalConfig:
    dataset_path: Path
    output_path: Path | None = None


def run_eval(config: EvalConfig) -> dict[str, Any]:
    if not config.dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {config.dataset_path}")

    return {
        "dataset": str(config.dataset_path),
        "output": str(config.output_path) if config.output_path else None,
        "status": "pending",
    }
