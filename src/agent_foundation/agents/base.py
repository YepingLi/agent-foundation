from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable

from ..providers.llm import LLMProvider


class BaseAgent(ABC):
    def __init__(self, name: str, llm: LLMProvider) -> None:
        self.name = name
        self.llm = llm
        self.tools: dict[str, Callable[..., Any]] = {}

    def add_tool(self, name: str, tool: Callable[..., Any]) -> None:
        self.tools[name] = tool

    @abstractmethod
    def run(self, input_text: str, **kwargs: Any) -> Any:
        raise NotImplementedError
