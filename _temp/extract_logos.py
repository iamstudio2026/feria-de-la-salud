import re

with open('dashboard-feria-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

output = []

# Extract base64 images and surrounding context
logo_matches = list(re.finditer(r'<img[^>]*src="(data:image[^"]+)"[^>]*>', content))
output.append(f'Found {len(logo_matches)} img tags with base64 src\n')

for i, m in enumerate(logo_matches):
    start = max(0, m.start()-300)
    context_before = content[start:m.start()]
    src = m.group(1)
    output.append(f'\n--- Image {i} ---')
    output.append(f'  base64 length: {len(src)} chars')
    output.append(f'  context before: ...{context_before[-200:]}')
    tag = m.group(0)
    alt_m = re.search(r'alt="([^"]*)"', tag)
    cls_m = re.search(r'class="([^"]*)"', tag)
    if alt_m: output.append(f'  alt="{alt_m.group(1)}"')
    if cls_m: output.append(f'  class="{cls_m.group(1)}"')

# Extract the header section
header_start = content.find('<header')
if header_start >= 0:
    header_end = content.find('</header>', header_start)
    if header_end >= 0:
        header_end += 10
    header_html = content[header_start:header_end]
    header_clean = re.sub(r'data:image/[^"]+', 'BASE64_DATA', header_html)
    output.append('\n\n=== HEADER SECTION (base64 replaced) ===')
    output.append(header_clean)

# Extract CSS variables/colors
style_start = content.find('<style')
if style_start >= 0:
    style_end = content.find('</style>', style_start)
    style_content = content[style_start:style_end+8]
    # Extract first 2000 chars of style
    output.append('\n\n=== STYLE SECTION (first 2000 chars) ===')
    output.append(style_content[:2000])

# Extract base64 for each logo and write to separate files
for i, m in enumerate(logo_matches):
    src = m.group(1)
    with open(f'logo_base64_{i}.txt', 'w', encoding='utf-8') as f:
        f.write(src)
    output.append(f'\nWrote logo_base64_{i}.txt ({len(src)} chars)')

with open('extract_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print('Done! Results in extract_results.txt')
