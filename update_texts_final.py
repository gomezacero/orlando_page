import os
import re

# ORLANDO
orlando_idx = r"C:\Users\Santiago\Documents\GitHub\orlando\index.html"
with open(orlando_idx, 'r', encoding='utf-8') as f:
    content = f.read()

new_about = r'''<div class="about-content">
            <span class="section-tag">Quiénes somos</span>
            <h2 id="nosotros-heading">Experiencia y Confianza Empresarial</h2>
            <p>En <strong>orlandorojasrodriguez.com</strong>, somos una plataforma comercial orientada a resultados, con más de 15 años de trayectoria construyendo, posicionando y escalando productos en el mercado colombiano. Nuestra experiencia nos ha permitido desarrollar un modelo propio basado en la combinación de estrategia, comunicación efectiva y ejecución ágil en múltiples canales de venta.</p>
            <p>Hemos consolidado un enfoque integral que abarca ventas online, atención presencial y dinámicas de alto impacto a través de medios de comunicación como radio, prensa, televisión y entornos digitales. Esta capacidad de integración nos permite conectar con el consumidor de manera directa, generando confianza, recordación y decisiones de compra en el momento oportuno.</p>
            <p>A lo largo de nuestra evolución, hemos entendido que el éxito comercial no depende únicamente del producto, sino de la forma en que se comunica, se posiciona y se acerca al cliente. Por eso, cada proceso que lideramos está enfocado en maximizar el alcance, optimizar la conversión y garantizar resultados sostenibles.</p>
            <p>Hoy, <strong>ORLANDO ROJAS RODRIGUEZ</strong> fortalece su operación liderando procesos comerciales a nivel nacional a través de <strong>Herbavid Colombia</strong>, nuestro principal canal de ventas de suplementos vitamínicos. Desde allí impulsamos estrategias innovadoras que potencian la visibilidad de las marcas, amplían su alcance y consolidan su presencia en el mercado.</p>
            <p>Trabajamos con una visión clara: transformar cada oportunidad en crecimiento, integrando experiencia, innovación y ejecución para seguir liderando en un entorno comercial competitivo.</p>
            <div class="about-badges">'''
content = re.sub(r'<div class="about-content">\s*<span class="section-tag">Quiénes somos</span>\s*<h2 id="nosotros-heading">.*?<div class="about-badges">', new_about, content, flags=re.DOTALL)
with open(orlando_idx, 'w', encoding='utf-8') as f:
    f.write(content)

orlando_ctc = r"C:\Users\Santiago\Documents\GitHub\orlando\contact.html"
with open(orlando_ctc, 'r', encoding='utf-8') as f:
    content = f.read()
new_contact = r'''<span class="section-tag">Sobre nosotros</span>
        <h2>ORLANDO ROJAS RODRIGUEZ</h2>
        <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
          Somos una plataforma comercial orientada a resultados con más de 15 años de trayectoria. <strong>ORLANDO ROJAS RODRIGUEZ</strong> ha consolidado un enfoque integral en ventas online, atención presencial y medios masivos. Hoy fortalecemos nuestra operación a nivel nacional a través de <strong>Herbavid Colombia</strong>, nuestro principal canal de ventas de suplementos vitamínicos, transformando cada oportunidad en crecimiento y liderazgo comercial.
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: .75rem; justify-content: center;">'''
content = re.sub(r'<span class="section-tag">Sobre nosotros</span>\s*<h2>ORLANDO ROJAS RODRIGUEZ</h2>.*?<div style="display: flex; flex-wrap: wrap; gap: \.75rem; justify-content: center;">', new_contact, content, flags=re.DOTALL)
with open(orlando_ctc, 'w', encoding='utf-8') as f:
    f.write(content)


# VIDACOL
vidacol_idx = r"C:\Users\Santiago\Documents\GitHub\vidacol\index.html"
with open(vidacol_idx, 'r', encoding='utf-8') as f:
    content = f.read()

new_vidacol_about = r'''<div class="about-content">
            <span class="section-tag">Nuestra Firma</span>
            <h2>Visión y Liderazgo</h2>
            <p>En <strong>VIDACOL</strong>, somos una plataforma comercial orientada a resultados, con más de 15 años de trayectoria construyendo, posicionando y escalando productos en el mercado colombiano. Nuestra experiencia nos ha permitido desarrollar un modelo propio basado en la combinación de estrategia, comunicación efectiva y ejecución ágil en múltiples canales de venta.</p>
            <p>Hemos consolidado un enfoque integral que abarca ventas online, atención presencial y dinámicas de alto impacto a través de medios de comunicación como radio, prensa, televisión y entornos digitales. Esta capacidad de integración nos permite conectar con el consumidor de manera directa, generando confianza, recordación y decisiones de compra en el momento oportuno.</p>
            <p>A lo largo de nuestra evolución, hemos entendido que el éxito comercial no depende únicamente del producto, sino de la forma en que se comunica, se posiciona y se acerca al cliente. Por eso, cada proceso que lideramos está enfocado en maximizar el alcance, optimizar la conversión y garantizar resultados sostenibles.</p>
            <p>Hoy, bajo la dirección de nuestra CEO <strong>Nayibe Lopez Serrano</strong>, fortalecemos nuestra operación liderando procesos comerciales a nivel nacional. A través de <strong>VIDACOL</strong>, nuestro principal canal de ventas de suplementos vitamínicos, impulsamos estrategias innovadoras que potencian la visibilidad de las marcas, amplían su alcance y consolidan su presencia en el mercado.</p>
            <p>Trabajamos con una visión clara: transformar cada oportunidad en crecimiento, integrando experiencia, innovación y ejecución para seguir liderando en un entorno comercial competitivo.</p>
          </div>
          <div class="info-card">'''
content = re.sub(r'<div class="about-content">\s*<span class="section-tag">Nuestra Firma</span>\s*<h2>Visión y Liderazgo</h2>.*?</div>\s*<div class="info-card">', new_vidacol_about, content, flags=re.DOTALL)
with open(vidacol_idx, 'w', encoding='utf-8') as f:
    f.write(content)

vidacol_ctc = r"C:\Users\Santiago\Documents\GitHub\vidacol\contact.html"
with open(vidacol_ctc, 'r', encoding='utf-8') as f:
    content = f.read()

new_vidacol_contact = r'''<div class="info-card" style="background: var(--primary); color: #fff; border: none;">
            <h3 style="color: #fff;">Acerca de VIDACOL</h3>
            <p style="color: #cbd5e1; margin-bottom: 20px; font-size: 1.1rem; line-height: 1.8;">
              Somos una plataforma comercial orientada a resultados, con más de 15 años de trayectoria posicionando productos en el mercado colombiano a través de canales online, presenciales y medios de comunicación masivos.
            </p>
            <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.8;">
              Bajo la dirección de nuestra <strong>CEO Nayibe Lopez Serrano</strong>, lideramos procesos comerciales a nivel nacional. A través de <strong>VIDACOL</strong> impulsamos estrategias innovadoras y la venta de suplementos vitamínicos, transformando cada oportunidad en crecimiento sostenido.
            </p>
          </div>'''
content = re.sub(r'<div class="info-card" style="background: var\(--primary\); color: #fff; border: none;">\s*<h3 style="color: #fff;">Acerca de VIDACOL</h3>.*?</div>', new_vidacol_contact, content, flags=re.DOTALL)
with open(vidacol_ctc, 'w', encoding='utf-8') as f:
    f.write(content)
