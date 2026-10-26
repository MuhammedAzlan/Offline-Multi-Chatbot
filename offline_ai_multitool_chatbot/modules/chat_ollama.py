import requests

def ask_ollama(prompt: str, model: str = "llama3.1:8b") -> str:
    """
    Requires Ollama running locally:
    ollama serve
    ollama pull llama3.1:8b
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Ollama error: {e}. Make sure Ollama is installed, running, and the model is downloaded."
