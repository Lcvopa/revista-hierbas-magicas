import re

emoji_map = {
    "Abedul": "🌳",
    "Ajenjo": "🌿",
    "Ajo": "🧄",
    "Albahaca": "🌿",
    "Alcanfor": "🧊",
    "Alfalfa": "🌱",
    "Algodón": "☁️",
    "Almendra": "🥜",
    "Aloe": "🌵",
    "Amapola": "🌺",
    "Anís": "🌟",
    "Apio": "🥬",
    "Arroz": "🍚",
    "Avena": "🌾",
    "Bambú": "��",
    "Banana": "🍌",
    "Benjuí": "💨",
    "Cactus": "🌵",
    "Calabaza": "🎃",
    "Canela": "🪵",
    "Caña de azúcar": "🎋",
    "Cañamomo": "🌿",
    "Cardamomo": "🫘",
    "Cebolla": "🧅",
    "Cedro": "🌲",
    "Cereales": "🌾",
    "Cereza": "🍒",
    "Clavel": "🌸",
    "Clavo": "🔨",
    "Coco": "🥥",
    "Comino": "🌱",
    "Copal": "🌫️",
    "Enebro": "🫐",
    "Eucalipto": "🐨",
    "Frambuesa": "🫐",
    "Fresa": "🍓",
    "Gardenia": "🌼",
    "Geranio": "🌸",
    "Ginseng": "🫚",
    "Girasol": "🌻",
    "Granada": "🍎",
    "Helecho": "🌿",
    "Hierbabuena": "🍃",
    "Jazmín": "🌼",
    "Laurel": "🌿",
    "Lila": "🌸",
    "Lima": "🍋",
    "Limón": "🍋",
    "Lirio": "⚜️",
    "Loto": "🪷",
    "Madreselva": "🌺",
    "Maíz": "🌽",
    "Mandrágora": "🌱",
    "Manzana": "🍎",
    "Mejorana": "🌿",
    "Menta": "🍃",
    "Milenrama": "🌿",
    "Mirra": "⚱️",
    "Muérdago": "🌿",
    "Naranja": "🍊",
    "Orquídea": "🌸",
    "Pachulí": "🌿",
    "Paja": "🌾",
    "Pino": "🌲",
    "Roble": "🌳",
    "Romero": "🌿",
    "Rosa": "🌹",
    "Ruda": "🌿",
    "Salvia": "🌿",
    "Sándalo": "🪵",
    "Sauce": "��",
    "Saúco": "🫐",
    "Trébol": "🍀",
    "Vainilla": "🍦",
    "Verbena": "🌸"
}

with open("index.html", "r") as f:
    content = f.read()

def replace_title(match):
    name_with_existing_emoji = match.group(1).strip()
    name = re.sub(r'[^\w\sñáéíóúÁÉÍÓÚ]', '', name_with_existing_emoji).strip()
    
    emoji = emoji_map.get(name, "🌿")
    new_title = f"{name} {emoji}"
    
    # Check if there is already an img tag right after
    # Because we don't want to double add or break things.
    # Actually, let's just replace the title text for now.
    return f'<h3 class="herb-title">{new_title}</h3>'

# Replace titles
content = re.sub(r'<h3 class="herb-title">(.*?)</h3>', replace_title, content)

def inject_emoji_images(match):
    full_match = match.group(0)
    title = match.group(1)
    
    # If there is already an img, don't inject
    if '<img' in full_match:
        return full_match
        
    name = re.sub(r'[^\w\sñáéíóúÁÉÍÓÚ]', '', title).strip()
    emoji = emoji_map.get(name, "🌿")
    
    emoji_img = f'<div class="herb-emoji-img">{emoji}</div>'
    
    return f'<h3 class="herb-title">{title}</h3>\n    {emoji_img}'

content = re.sub(r'<h3 class="herb-title">(.*?)</h3>(\s*)<div class="herb-details">', inject_emoji_images, content)

with open("index.html", "w") as f:
    f.write(content)

print("Done replacing.")
