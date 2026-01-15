from __future__ import annotations

import logging
from typing import Optional


def setup_logging(level: str = "INFO") -> logging.Logger:
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
    return logging.getLogger("agent_foundation")


def get_logger(name: Optional[str] = None) -> logging.Logger:
    return logging.getLogger(name or "agent_foundation")
