# agent-foundation

Shared foundation primitives for LLM providers, retrieval, tools, agents, evaluation, and observability.

## Setup (repeatable)

1) Create and activate a virtual environment
```sh
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3) Configure your Gemini API key
```sh
export GEMINI_API_KEY="your_key_here"
```

Add the same line to `~/.zshrc` or `~/.bashrc` to make it persistent.
