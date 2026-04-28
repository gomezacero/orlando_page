import os

repo_dir_vidacol = r'C:\Users\Santiago\Documents\GitHub\vidacol'

index_path = os.path.join(repo_dir_vidacol, 'index.html')
contact_path = os.path.join(repo_dir_vidacol, 'contact.html')

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Update "Nosotros" section in Vidacol to reflect commercialization experience
old_about = """            <p>
              En <strong>VIDACOL</strong> nos dedicamos a ofrecer soluciones de asesoría nacional con un enfoque holístico hacia el éxito corporativo. Creemos que las organizaciones alcanzan su máximo potencial cuando cuidan todos sus frentes.
            </p>
            <p>
              Liderada por nuestra <strong>CEO Nayibe Lopez Serrano</strong>, la organización se destaca por su riguroso compromiso con la excelencia empresarial. Entendemos que el rendimiento óptimo de una organización va de la mano con el bienestar físico y mental de sus integrantes.
            </p>
            <p>
              Por ello, además de nuestros servicios de consultoría estratégica, contamos con un sólido portafolio de distribución y venta de suplementos vitamínicos de alta calidad, apoyando la salud integral como pilar fundamental del desarrollo profesional.
            </p>"""

new_about = """            <p>
              En <strong>VIDACOL</strong> consolidamos años de experiencia en el ámbito comercial y de asesoría nacional, construyendo un modelo de negocio sólido y adaptable. Nuestra trayectoria nos ha permitido identificar oportunidades clave en distintos canales de venta, destacándonos en estrategias online y ventas minoristas enfocadas en resultados.
            </p>
            <p>
              Liderada por nuestra <strong>CEO Nayibe Lopez Serrano</strong>, la organización se caracteriza por combinar un profundo conocimiento del mercado con estrategias de posicionamiento efectivas. Entendemos que el crecimiento de una empresa va de la mano con soluciones logísticas ágiles y el bienestar integral de sus clientes.
            </p>
            <p>
              Por ello, además de nuestra consultoría, ejecutamos procesos comerciales de alto impacto a través de nuestro sólido portafolio de distribución y venta de suplementos vitamínicos, conectando marcas con consumidores de manera directa y apoyando la salud como pilar fundamental.
            </p>"""

# Fix encoding issue with replacing
# Because we read with utf-8, but sometimes file has slightly different line endings, we should use a simpler replace or read lines.
# We'll just replace the text chunks directly. To be safe, we can use regex or simpler string replacement.
index_content = index_content.replace(old_about, new_about)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

with open(contact_path, 'r', encoding='utf-8') as f:
    contact_content = f.read()

old_contact_about = """            <p style="color: #cbd5e1; margin-bottom: 20px; font-size: 1.1rem; line-height: 1.8;">
              Somos una firma de asesoría nacional profundamente comprometida con el desarrollo empresarial sostenible de nuestros clientes.
            </p>
            <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.8;">
              Bajo la visión estratégica y dirección de nuestra <strong>CEO Nayibe Lopez Serrano</strong>, también promovemos la salud corporativa mediante nuestra división especializada en la distribución de suplementos vitamínicos, integrando así productividad y bienestar humano.
            </p>"""

new_contact_about = """            <p style="color: #cbd5e1; margin-bottom: 20px; font-size: 1.1rem; line-height: 1.8;">
              Con una destacada trayectoria en el ámbito comercial, logístico y de asesoría nacional, <strong>VIDACOL</strong> está profundamente comprometida con el crecimiento estratégico y las ventas minoristas.
            </p>
            <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.8;">
              Bajo la dirección de nuestra <strong>CEO Nayibe Lopez Serrano</strong>, también lideramos procesos de comercialización de alto impacto mediante nuestra división de suplementos vitamínicos, integrando bienestar integral y éxito comercial.
            </p>"""

contact_content = contact_content.replace(old_contact_about, new_contact_about)

with open(contact_path, 'w', encoding='utf-8') as f:
    f.write(contact_content)

