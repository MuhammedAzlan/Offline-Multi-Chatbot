from pathlib import Path
import uuid, textwrap

def make_simple_video(title: str, script: str, output_dir: Path) -> str:
    """
    Creates a simple text-based video.
    Install:
    pip install moviepy pillow
    For real voice, first generate voice using /api/voice, then attach audio manually or extend this module.
    """
    output_dir.mkdir(exist_ok=True)
    file_name = f"video_{uuid.uuid4().hex[:8]}.mp4"
    path = output_dir / file_name

    try:
        from PIL import Image, ImageDraw, ImageFont
        from moviepy.editor import ImageClip

        W, H = 1080, 1920
        img = Image.new("RGB", (W, H), (18, 24, 38))
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("arial.ttf", 64)
            font_body = ImageFont.truetype("arial.ttf", 38)
        except:
            font_title = ImageFont.load_default()
            font_body = ImageFont.load_default()

        draw.text((70, 160), title, fill=(255, 255, 255), font=font_title)
        wrapped = textwrap.wrap(script, width=38)
        y = 320
        for line in wrapped[:24]:
            draw.text((70, y), line, fill=(225, 231, 239), font=font_body)
            y += 58

        image_path = output_dir / f"frame_{uuid.uuid4().hex[:8]}.jpg"
        img.save(image_path, quality=95)

        clip = ImageClip(str(image_path)).set_duration(8)
        clip.write_videofile(str(path), fps=24, codec="libx264", audio=False, verbose=False, logger=None)
        return str(path)
    except Exception as e:
        fallback = path.with_suffix(".txt")
        fallback.write_text(f"Video generation error: {e}\n\nInstall moviepy and pillow.\n\nTitle: {title}\nScript: {script}", encoding="utf-8")
        return str(fallback)
