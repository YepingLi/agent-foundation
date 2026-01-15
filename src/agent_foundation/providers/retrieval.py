from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Iterable


@dataclass(frozen=True)
class RetrievalResult:
    id: str
    score: float
    payload: dict[str, Any]


class Retriever(ABC):
    name: str

    @abstractmethod
    def search(self, query: str, **kwargs: Any) -> Iterable[RetrievalResult]:
        raise NotImplementedError


class RetrievalRegistry:
    def __init__(self) -> None:
        self._factories: dict[str, Callable[[], Retriever]] = {}

    def register(self, name: str, factory: Callable[[], Retriever]) -> None:
        key = name.strip().lower()
        if not key:
            raise ValueError("Retriever name must be non-empty")
        self._factories[key] = factory

    def create(self, name: str) -> Retriever:
        key = name.strip().lower()
        if key not in self._factories:
            raise KeyError(f"Retriever not registered: {name}")
        return self._factories[key]()

    def list(self) -> list[str]:
        return sorted(self._factories.keys())
