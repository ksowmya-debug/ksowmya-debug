import os
import xml.etree.ElementTree as ET

files = ['assets/about-card.svg', 'assets/tech-row2.svg']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix duplicates up to 5 times just in case
    for _ in range(5):
        content = content.replace('class="text-primary" class="text-primary"', 'class="text-primary"')
        content = content.replace('class="text-secondary" class="text-secondary"', 'class="text-secondary"')
        content = content.replace('class="stroke-secondary" class="stroke-secondary"', 'class="stroke-secondary"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    # Validate
    try:
        ET.fromstring(content)
        print(f"{filepath} is now VALID.")
    except Exception as e:
        print(f"Error validating {filepath}: {e}")
