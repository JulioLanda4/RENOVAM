from pathlib import Path
text = Path('proyectos/index.qmd').read_text(encoding='utf-8')
replacements = {
    'categorÃ­a': 'categoría',
    'diseÃ±o': 'diseño',
    'gestiÃ³n': 'gestión',
    'instalaciÃ³n': 'instalación',
    'monitoreo continuo.': 'monitoreo continuo.',
    'operaciÃ³n': 'operación',
    'solares hÃ­bridos': 'solares híbridos',
    'conmutaciÃ³n': 'conmutación',
    'autÃ³nomos': 'autónomos',
    'energÃ­a': 'energía',
    'pÃºblica': 'pública',
    'lÃ­neas': 'líneas',
    'Tu navegador no soporta la reproducciÃ³n del video.': 'Tu navegador no soporta la reproducción del video.'
}
for bad, good in replacements.items():
    text = text.replace(bad, good)
Path('proyectos/index.qmd').write_text(text, encoding='utf-8')
