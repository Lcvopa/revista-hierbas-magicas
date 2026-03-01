import re

with open('content.txt', 'r', encoding='utf-8') as f:
    text = f.read()

herb_names = [
    "Abedul", "Aguacate", "Ajenjo", "Ajo", "Albahaca", "Alcanfor", "Alfalfa", "Algodón", "Almendra", "Aloe", "Amapola", "Anís", "Apio", "Arroz", "Avena",
    "Bambú", "Banana", "Benjuí", "Cactus", "Calabaza", "Canela", "Caña de azúcar", "Cañamomo", "Cardamomo", "Cebolla", "Cedro", "Cereales", "Cereza", "Clavel", "Clavo", "Coco", "Comino", "Copal",
    "Enebro", "Eucalipto", "Frambuesa", "Fresa",
    "Gardenia", "Geranio", "Ginseng", "Girasol", "Granada",
    "Helecho", "Hierbabuena", "Jazmín",
    "Laurel", "Lila", "Lima", "Limón", "Lirio", "Loto",
    "Madreselva", "Maíz", "Mandrágora", "Manzana", "Mejorana", "Menta", "Milenrama", "Mirra", "Muérdago",
    "Naranja", "Orquídea", "Pachulí", "Paja", "Pino",
    "Roble", "Romero", "Rosa", "Ruda",
    "Salvia", "Sándalo", "Sauce", "Saúco",
    "Trébol", "Vainilla", "Verbena"
]

# Create a regex to split exactly at these names
pattern = r'(?m)^(' + '|'.join(herb_names) + r')(?:\s*\(.*?\))?\s*(?:\nVENENOSO)?\n'

parts = re.split(pattern, text)

pages = []
current_page = ""
count = 0

for i in range(1, len(parts), 2):
    name = parts[i].strip()
    content = parts[i+1].strip()
    
    # Simple formatting
    lines = content.split('\n')
    formatted_content = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('Genero:') or line.startswith('Planeta:') or line.startswith('Elemento:') or line.startswith('Deidad:') or line.startswith('Deidades:'):
            formatted_content += f'<p class="meta-data"><strong>{line.split(":", 1)[0]}:</strong> {line.split(":", 1)[1].strip()}</p>\n'
        elif line.startswith('Usos mágicos:'):
            formatted_content += f'<p class="magic-uses"><strong>Usos mágicos:</strong> {line.split(":", 1)[1].strip()}</p>\n'
        else:
            if formatted_content.endswith('</p>\n'):
                # Append to previous paragraph if it was uses
                formatted_content = formatted_content[:-5] + ' ' + line + '</p>\n'
            else:
                formatted_content += f'<p>{line}</p>\n'

    import os
    img_path = f'assets/herb_{name.lower().replace(" ", "_")}.png'
    img_tag = ""
    if os.path.exists(img_path):
        img_tag = f'<img src="{img_path}" alt="{name}" class="herb-img">'

    entry = f'''<div class="herb-entry">
    <h3 class="herb-title">{name}</h3>
    <div class="herb-details">
        {img_tag}
        {formatted_content}
    </div>
</div>
'''
    current_page += entry
    count += 1
    
    # Control how much goes on a page so it doesn't overflow
    if len(current_page) > 600 or count >= 1:
        pages.append(current_page)
        current_page = ""
        count = 0

if current_page:
    pages.append(current_page)

html_pages = ""
for i, p in enumerate(pages):
    # Front and back of each leaf
    html_pages += f'''<div class="page" data-density="soft">
    <div class="page-content">
        <div class="page-wrap">
            {p}
        </div>
        <div class="page-footer"> - {i+4} - </div>
    </div>
</div>
'''

print(html_pages)
