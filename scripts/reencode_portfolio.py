from pathlib import Path
path = Path('proyectos/index.qmd')
text = path.read_bytes().decode('latin-1')
path.write_text(text, encoding='utf-8')
