import os

repo_dir = r"C:\Users\Santiago\Documents\GitHub\vidacol"
files = ["index.html", "contact.html"]

for filename in files:
    filepath = os.path.join(repo_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace("contacto@vidalcol.com", "contacto@vidacol.com.co")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

cname_path = os.path.join(repo_dir, "CNAME")
with open(cname_path, 'w', encoding='utf-8') as f:
    f.write("vidacol.com.co\n")
