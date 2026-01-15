from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any


class ToolStatus(str, Enum):
    OK = "ok"
    ERROR = "error"
    RETRY = "retry"


@dataclass(frozen=True)
class ToolError:
    code: str
    message: str
    detail: dict[str, Any] | None = None


@dataclass(frozen=True)
class ToolResult:
    status: ToolStatus
    data: Any | None = None
    error: ToolError | None = None


def ok(data: Any | None = None) -> ToolResult:
    return ToolResult(status=ToolStatus.OK, data=data)


def error(code: str, message: str, detail: dict[str, Any] | None = None) -> ToolResult:
    return ToolResult(
        status=ToolStatus.ERROR,
        error=ToolError(code=code, message=message, detail=detail),
    )
