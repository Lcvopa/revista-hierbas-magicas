import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

parts = html.split('<!-- The Herbs Pages -->')
before_herbs = parts[0] + '<!-- The Herbs Pages -->\n'
rest = parts[1]

pages = re.split(r'(?=<div class="page")', rest)

herb_pages = []
back_covers = []
for p in pages:
    if not p.strip():
        continue
    if 'back-cover' in p or 'Inside Back Cover' in p or 'El Fin' in p or 'PageFlip.js' in p:
        back_covers.append(p)
    elif 'herb-title' in p:
        herb_pages.append(p)
    else:
        back_covers.append(p)

toc = []
for i, p in enumerate(herb_pages):
    titles = re.findall(r'<h3 class="herb-title">(.*?)</h3>', p)
    for title in titles:
        toc.append((title, i))

ITEMS_PER_PAGE = 26
num_index_pages = (len(toc) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
first_herb_page_num = 4 + num_index_pages

index_pages_html = ""
for page_idx in range(num_index_pages):
    start = page_idx * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    items = toc[start:end]
    
    index_content = '<h2 class="index-title" style="text-align:center; color: var(--gold); font-family: var(--font-heading); margin-bottom: 20px; font-size: 2rem;">Índice</h2>\n'
    index_content += '<ul class="index-list" style="list-style: none; padding: 0; font-size: 1.1rem; line-height: 1.8; font-family: var(--font-body);">\n'
    for title, rel_page in items:
        actual_page_num = first_herb_page_num + rel_page
        index_content += f'<li style="display: flex; justify-content: space-between; border-bottom: 1px dotted rgba(0,0,0,0.2); margin-bottom: 8px;"><span>{title}</span> <span style="font-weight: bold; color: var(--accent);">{actual_page_num}</span></li>\n'
    index_content += '</ul>\n'
    
    current_page_num = 4 + page_idx
    
    index_page = f'''<div class="page" data-density="soft">
    <div class="page-content">
        <div class="page-wrap">
            {index_content}
        </div>
        <div class="page-footer"> - {current_page_num} - </div>
    </div>
</div>
'''
    index_pages_html += index_page

updated_herb_pages = []
for i, p in enumerate(herb_pages):
    new_page_num = first_herb_page_num + i
    p = re.sub(r'<div class="page-footer"> - \d+ - </div>', f'<div class="page-footer"> - {new_page_num} - </div>', p)
    updated_herb_pages.append(p)

final_html = before_herbs + index_pages_html + "".join(updated_herb_pages) + "".join(back_covers)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Generated {num_index_pages} index pages. First herb is now on page {first_herb_page_num}.")
