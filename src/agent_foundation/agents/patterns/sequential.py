from __future__ import annotations

from typing import Any, Callable


class SequentialRunner:
    def __init__(self, steps: list[Callable[[Any], Any]]) -> None:
        self.steps = steps

    def run(self, input_data: Any) -> list[Any]:
        outputs: list[Any] = []
        current = input_data
        for step in self.steps:
            current = step(current)
            outputs.append(current)
        return outputs
