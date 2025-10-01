# RENOVAM • Sitio web

Repositorio del sitio de RENOVAM construido con Quarto.

## Flujo de trabajo

1. Instala [Quarto](https://quarto.org/) en tu máquina.
2. Ejecuta <code>quarto preview</code> para revisar cambios locales.
3. Ejecuta <code>quarto render</code> para generar la versión estática. La salida queda en <code>docs/</code> lista para GitHub Pages.

## Despliegue en GitHub Pages

- En la configuración del repositorio selecciona la rama que desees publicar y el folder <code>docs/</code> como fuente de Pages.
- Cada vez que hagas <code>quarto render</code>, confirma que los nuevos archivos en <code>docs/</code> se suben junto con el resto del código.

## Estructura de contenidos

- <code>Recursos/</code>: Biblioteca original de imágenes y videos usada por las páginas.
- <code>styles/custom.css</code>: Hoja de estilos principal del sitio.
- Archivos <code>*.qmd</code>: Páginas del sitio escritas en Quarto/Markdown con bloques HTML personalizados.

Happy hacking ⚡
