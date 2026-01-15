from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Iterable


@dataclass(frozen=True)
class LLMResult:
    text: str
    raw: Any | None = None
    usage: dict[str, Any] | None = None


class LLMProvider(ABC):
    name: str

    @abstractmethod
    def generate(self, prompt: str, **kwargs: Any) -> LLMResult:
        raise NotImplementedError

    def stream(self, prompt: str, **kwargs: Any) -> Iterable[str]:
        raise NotImplementedError


class LLMRegistry:
    def __init__(self) -> None:
        self._factories: dict[str, Callable[[], LLMProvider]] = {}

    def register(self, name: str, factory: Callable[[], LLMProvider]) -> None:
        key = name.strip().lower()
        if not key:
            raise ValueError("LLM provider name must be non-empty")
        self._factories[key] = factory

    def create(self, name: str) -> LLMProvider:
        key = name.strip().lower()
        if key not in self._factories:
            raise KeyError(f"LLM provider not registered: {name}")
        return self._factories[key]()

    def list(self) -> list[str]:
        return sorted(self._factories.keys())
