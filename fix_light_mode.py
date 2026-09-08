import os

def fix_svg(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    style_block = '''  <style>
    @media (prefers-color-scheme: light) {
      .text-primary { fill: #0f172a !important; }
      .text-secondary { fill: #475569 !important; }
      .stroke-secondary { stroke: #475569 !important; }
    }
  </style>'''

    if '<style>' not in content:
        content = content.replace('<defs>', style_block + '\n  <defs>')

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix about-card.svg
fix_svg('assets/about-card.svg', {
    'fill="#f8fafc"': 'class="text-primary" fill="#f8fafc"',
    'fill="#94a3b8"': 'class="text-secondary" fill="#94a3b8"'
})

# Fix tech-row2.svg
fix_svg('assets/tech-row2.svg', {
    'fill="#cbd5e1"': 'class="text-secondary" fill="#cbd5e1"',
    'stroke="#cbd5e1"': 'class="stroke-secondary" stroke="#cbd5e1"'
})

print('Updated SVGs for Light Mode compatibility!')
