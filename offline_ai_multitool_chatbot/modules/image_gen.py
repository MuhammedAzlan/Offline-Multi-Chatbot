from pathlib import Path
import uuid

def generate_image(prompt: str, output_dir: Path) -> str:
    """
    Offline image generation requires Stable Diffusion.
    Recommended advanced setup:
    1. Install AUTOMATIC1111 Stable Diffusion WebUI OR ComfyUI
    2. Run it locally
    3. Connect this function to its local API

    This starter creates a placeholder file if Stable Diffusion API is not configured.
    """
    output_dir.mkdir(exist_ok=True)
    file_name = f"image_prompt_{uuid.uuid4().hex[:8]}.txt"
    path = output_dir / file_name
    path.write_text(
        "Image generation module is ready for integration.\n\n"
        "To make real images offline, install Stable Diffusion WebUI or ComfyUI and connect its API.\n\n"
        f"Prompt:\n{prompt}",
        encoding="utf-8"
    )
    return str(path)
