from pathlib import Path
import html, uuid

def make_html_file(title: str, content: str, output_dir: Path) -> str:
    output_dir.mkdir(exist_ok=True)
    file_name = f"page_{uuid.uuid4().hex[:8]}.html"
    safe_title = html.escape(title)
    safe_content = html.escape(content).replace("\n", "<br>")
    page = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{safe_title}</title>
<style>
body {{
    font-family: Arial, sans-serif;
    background: #f5f7fb;
    color: #111827;
    padding: 40px;
}}
.card {{
    max-width: 850px;
    margin: auto;
    background: white;
    border-radius: 18px;
    padding: 36px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
}}
h1 {{
    margin-top: 0;
}}
</style>
</head>
<body>
<div class="card">
<h1>{safe_title}</h1>
<p>{safe_content}</p>
</div>
</body>
</html>"""
    path = output_dir / file_name
    path.write_text(page, encoding="utf-8")
    return str(path)

def make_pdf_file(title: str, content: str, output_dir: Path) -> str:
    """
    Uses reportlab. Install:
    pip install reportlab
    """
    output_dir.mkdir(exist_ok=True)
    file_name = f"document_{uuid.uuid4().hex[:8]}.pdf"
    path = output_dir / file_name

    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet

        doc = SimpleDocTemplate(str(path), pagesize=A4)
        styles = getSampleStyleSheet()
        story = [
            Paragraph(title, styles["Title"]),
            Spacer(1, 16),
        ]

        for line in content.splitlines():
            story.append(Paragraph(line if line.strip() else " ", styles["BodyText"]))
            story.append(Spacer(1, 8))

        doc.build(story)
        return str(path)
    except Exception as e:
        fallback = path.with_suffix(".txt")
        fallback.write_text(f"PDF generation error: {e}\n\n{title}\n\n{content}", encoding="utf-8")
        return str(fallback)
