from flask import Flask, render_template, request, jsonify, send_from_directory
from pathlib import Path
import time, uuid, os

from modules.chat_ollama import ask_ollama
from modules.html_pdf import make_html_file, make_pdf_file
from modules.voice_tts import make_voice
from modules.video_maker import make_simple_video
from modules.image_gen import generate_image

app = Flask(__name__)
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "").strip()
    model = data.get("model", "llama3.1:8b").strip() or "llama3.1:8b"
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    answer = ask_ollama(prompt, model=model)
    return jsonify({"answer": answer})

@app.route("/api/html", methods=["POST"])
def html_file():
    data = request.get_json(force=True)
    title = data.get("title", "Generated Page")
    content = data.get("content", "")
    path = make_html_file(title, content, OUTPUT_DIR)
    return jsonify({"file": f"/outputs/{Path(path).name}"})

@app.route("/api/pdf", methods=["POST"])
def pdf_file():
    data = request.get_json(force=True)
    title = data.get("title", "Generated PDF")
    content = data.get("content", "")
    path = make_pdf_file(title, content, OUTPUT_DIR)
    return jsonify({"file": f"/outputs/{Path(path).name}"})

@app.route("/api/voice", methods=["POST"])
def voice():
    data = request.get_json(force=True)
    text = data.get("text", "")
    path = make_voice(text, OUTPUT_DIR)
    return jsonify({"file": f"/outputs/{Path(path).name}"})

@app.route("/api/video", methods=["POST"])
def video():
    data = request.get_json(force=True)
    title = data.get("title", "AI Video")
    script = data.get("script", "")
    path = make_simple_video(title, script, OUTPUT_DIR)
    return jsonify({"file": f"/outputs/{Path(path).name}"})

@app.route("/api/image", methods=["POST"])
def image():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "")
    path = generate_image(prompt, OUTPUT_DIR)
    return jsonify({"file": f"/outputs/{Path(path).name}"})

@app.route("/outputs/<path:filename>")
def outputs(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
