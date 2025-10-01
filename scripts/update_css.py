from pathlib import Path

path = Path('styles/custom.css')
base = path.read_text(encoding='utf-8').splitlines()

filtered = []
skip = False
for line in base:
    if line.strip().startswith('.portfolio-grid') or line.strip().startswith('.portfolio-carousel') or line.strip().startswith('.portfolio-slide') or line.strip().startswith('.portfolio-media') or line.strip().startswith('.portfolio-item'):
        skip = True
    if skip and line.strip() == '':
        skip = False
        continue
    if not skip:
        filtered.append(line)

styles = '\n'.join(filtered)

new_block = """
/* Portfolio showcase styles */
.portfolio-showcase {
  max-width: 1100px;
  margin: 0 auto 2.5rem;
  background: #ffffff;
  border-radius: 1.5rem;
  box-shadow: 0 24px 48px rgba(27, 34, 49, 0.15);
  border: 1px solid rgba(27, 34, 49, 0.1);
}

.portfolio-slide-row {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  padding: 2rem 2.5rem;
}

.portfolio-item-card {
  flex: 1 1 260px;
  max-width: 320px;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.portfolio-media-wrapper {
  position: relative;
  width: 100%;
  padding-top: 70%;
  border-radius: 1.1rem;
  overflow: hidden;
  background: #11151d;
}

.portfolio-media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.portfolio-item-caption {
  font-size: 0.95rem;
  font-weight: 600;
  color: #1b2231;
  text-align: center;
}

.portfolio-showcase .carousel-indicators {
  margin-bottom: 1.5rem;
}

.portfolio-showcase .carousel-indicators button {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: rgba(27, 34, 49, 0.3);
}

.portfolio-showcase .carousel-indicators .active {
  background-color: #1b2231;
}

.portfolio-showcase .carousel-control-prev,
.portfolio-showcase .carousel-control-next {
  width: 3rem;
  color: #1b2231;
}

.portfolio-showcase .carousel-control-prev-icon,
.portfolio-showcase .carousel-control-next-icon {
  filter: invert(15%) sepia(9%) saturate(604%) hue-rotate(176deg) brightness(95%) contrast(89%);
}

@media (max-width: 900px) {
  .portfolio-slide-row {
    flex-wrap: wrap;
    padding: 1.5rem;
  }

  .portfolio-item-card {
    flex: 1 1 220px;
    max-width: 260px;
  }
}
"""

path.write_text(styles + '\n' + new_block, encoding='utf-8')
