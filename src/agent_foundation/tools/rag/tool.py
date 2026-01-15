from __future__ import annotations

from typing import Any

from ...providers.llm import LLMProvider
from ...providers.retrieval import Retriever
from ..common import ToolResult, ok


class RagTool:
    def __init__(self, retriever: Retriever, llm: LLMProvider) -> None:
        self._retriever = retriever
        self._llm = llm

    def answer(self, query: str, top_k: int = 5, **kwargs: Any) -> ToolResult:
        results = list(self._retriever.search(query, **kwargs))[:top_k]
        context = "\n\n".join(
            str(item.payload.get("text", item.payload)) for item in results
        )
        prompt = (
            "Answer the question using the context. "
            "If context is missing, say you do not know.\n\n"
            f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        )
        llm_result = self._llm.generate(prompt)
        return ok(
            {
                "answer": llm_result.text,
                "sources": results,
                "raw": llm_result.raw,
                "usage": llm_result.usage,
            }
        )
