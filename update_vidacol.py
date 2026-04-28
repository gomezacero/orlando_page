import os

files = [
    r"C:\Users\Santiago\Documents\GitHub\vidacol\index.html",
    r"C:\Users\Santiago\Documents\GitHub\vidacol\contact.html"
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update brand and name
    content = content.replace("Nayib López", "Nayibe Lopez Serrano")
    # Carefully replace "Vidalcol" to "VIDACOL", except maybe in URLs.
    content = content.replace("Vidalcol", "VIDACOL")

    # 2. Update index.html
    if "index.html" in filepath:
        old_legal = """              <li>
                <span class="info-label">Razón Social</span>
                <span class="info-value">VIDACOL</span>
              </li>
              <li>
                <span class="info-label">Representante / CEO</span>
                <span class="info-value">Nayibe Lopez Serrano</span>
              </li>
              <li>
                <span class="info-label">Cobertura</span>
                <span class="info-value">Nacional (Colombia)</span>
              </li>"""
              
        new_legal = """              <li>
                <span class="info-label">Razón Social</span>
                <span class="info-value">VIDACOL</span>
              </li>
              <li>
                <span class="info-label">NIT</span>
                <span class="info-value">37751569-5</span>
              </li>
              <li>
                <span class="info-label">Representante / CEO</span>
                <span class="info-value">Nayibe Lopez Serrano</span>
              </li>
              <li>
                <span class="info-label">Dirección</span>
                <span class="info-value">Calle 45A #22-92 centro</span>
              </li>
              <li>
                <span class="info-label">Actividades</span>
                <span class="info-value">Soluciones logísticas, ventas minoristas</span>
              </li>
              <li>
                <span class="info-label">Cobertura</span>
                <span class="info-value">Nacional (Colombia)</span>
              </li>"""
        content = content.replace(old_legal, new_legal)

    # 3. Update contact.html
    if "contact.html" in filepath:
        old_info = """              <li>
                <span class="info-label">Empresa</span>
                <span class="info-value">VIDACOL</span>
              </li>
              <li>
                <span class="info-label">CEO y Fundadora</span>
                <span class="info-value">Nayibe Lopez Serrano</span>
              </li>
              <li>
                <span class="info-label">Área de Operación</span>
                <span class="info-value">Nacional (Colombia)</span>
              </li>"""
              
        new_info = """              <li>
                <span class="info-label">Empresa</span>
                <span class="info-value">VIDACOL</span>
              </li>
              <li>
                <span class="info-label">NIT</span>
                <span class="info-value">37751569-5</span>
              </li>
              <li>
                <span class="info-label">CEO y Fundadora</span>
                <span class="info-value">Nayibe Lopez Serrano</span>
              </li>
              <li>
                <span class="info-label">Dirección</span>
                <span class="info-value">Calle 45A #22-92 centro</span>
              </li>
              <li>
                <span class="info-label">Actividades</span>
                <span class="info-value">Soluciones logísticas, ventas minoristas</span>
              </li>
              <li>
                <span class="info-label">Área de Operación</span>
                <span class="info-value">Nacional (Colombia)</span>
              </li>"""
        content = content.replace(old_info, new_info)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
