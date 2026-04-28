import os
import shutil

# Paths
orlando_dir = r"C:\Users\Santiago\Documents\GitHub\orlando"
vidacol_dir = r"C:\Users\Santiago\Documents\GitHub\vidacol"

orlando_img_dir = os.path.join(orlando_dir, "assets", "images")
vidacol_img_dir = os.path.join(vidacol_dir, "assets", "images")

os.makedirs(orlando_img_dir, exist_ok=True)
os.makedirs(vidacol_img_dir, exist_ok=True)

herbavid_src = r"C:\Users\Santiago\Downloads\herbavid.png"
vidacol_src = r"C:\Users\Santiago\Downloads\vidacol.png"

shutil.copy(herbavid_src, os.path.join(orlando_img_dir, "herbavid.png"))
shutil.copy(vidacol_src, os.path.join(vidacol_img_dir, "vidacol.png"))

# ORLANDO UPDATES
orlando_idx = os.path.join(orlando_dir, "index.html")
with open(orlando_idx, 'r', encoding='utf-8') as f:
    content = f.read()
    
# Insert herbavid logo before the about-badges
herbavid_img_html = '''<div style="text-align: center; margin: 2rem 0;">
              <img src="assets/images/herbavid.png" alt="Herbavid Colombia" style="max-width: 250px; height: auto;">
            </div>
            <div class="about-badges">'''
content = content.replace('<div class="about-badges">', herbavid_img_html)
with open(orlando_idx, 'w', encoding='utf-8') as f:
    f.write(content)

orlando_ctc = os.path.join(orlando_dir, "contact.html")
with open(orlando_ctc, 'r', encoding='utf-8') as f:
    content = f.read()
# Insert herbavid logo after the description
herbavid_ctc_html = '''</p>
        <div style="text-align: center; margin-bottom: 2rem;">
          <img src="assets/images/herbavid.png" alt="Herbavid Colombia" style="max-width: 200px; height: auto;">
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: .75rem; justify-content: center;">'''
content = content.replace('</p>\n        <div style="display: flex; flex-wrap: wrap; gap: .75rem; justify-content: center;">', herbavid_ctc_html)
with open(orlando_ctc, 'w', encoding='utf-8') as f:
    f.write(content)


# VIDACOL UPDATES
vidacol_idx = os.path.join(vidacol_dir, "index.html")
vidacol_ctc = os.path.join(vidacol_dir, "contact.html")

def update_vidacol_header(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_logo = '''<a href="index.html" class="site-logo">
        <span class="logo-name">VIDACOL</span>
        <span class="logo-tag">Asesoría Nacional</span>
      </a>'''
      
    new_logo = '''<a href="index.html" class="site-logo" style="display: flex; align-items: center; gap: 12px; text-decoration: none;">
        <img src="assets/images/vidacol.png" alt="Logo Vidacol" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <div style="display: flex; flex-direction: column;">
          <span class="logo-name" style="margin-bottom: 0;">VIDACOL</span>
          <span class="logo-tag">Asesoría Nacional</span>
        </div>
      </a>'''
    
    content = content.replace(old_logo, new_logo)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_vidacol_header(vidacol_idx)
update_vidacol_header(vidacol_ctc)

# Add Vidacol image to the about section in index
with open(vidacol_idx, 'r', encoding='utf-8') as f:
    content = f.read()
vidacol_about_img = '''<div style="text-align: center; margin: 2rem 0;">
              <img src="assets/images/vidacol.png" alt="Vidacol" style="max-width: 200px; border-radius: 50%; box-shadow: 0 10px 30px -5px rgba(0,0,0,0.1);">
            </div>
          </div>
          <div class="info-card">'''
content = content.replace('</div>\n          <div class="info-card">', vidacol_about_img)
with open(vidacol_idx, 'w', encoding='utf-8') as f:
    f.write(content)

# Add Vidacol image to the about section in contact
with open(vidacol_ctc, 'r', encoding='utf-8') as f:
    content = f.read()
vidacol_ctc_img = '''</p>
            <div style="text-align: center; margin-top: 2rem;">
              <img src="assets/images/vidacol.png" alt="Vidacol" style="max-width: 150px; border-radius: 50%; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            </div>
          </div>'''
content = content.replace('</p>\n          </div>', vidacol_ctc_img)
with open(vidacol_ctc, 'w', encoding='utf-8') as f:
    f.write(content)
