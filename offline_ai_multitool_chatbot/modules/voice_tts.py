from pathlib import Path
import uuid

def make_voice(text: str, output_dir: Path) -> str:
    """
    Offline TTS using pyttsx3.
    Install:
    pip install pyttsx3
    On Windows it uses installed system voices.
    """
    output_dir.mkdir(exist_ok=True)
    file_name = f"voice_{uuid.uuid4().hex[:8]}.mp3"
    path = output_dir / file_name

    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 155)
        engine.setProperty("volume", 1.0)
        engine.save_to_file(text, str(path))
        engine.runAndWait()
        return str(path)
    except Exception as e:
        fallback = path.with_suffix(".txt")
        fallback.write_text(f"TTS error: {e}\n\nInstall pyttsx3 or configure system voices.\n\nText:\n{text}", encoding="utf-8")
        return str(fallback)
