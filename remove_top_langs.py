import re
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<div align="center">\s*<img src="[^"]*top-langs[^"]*" alt="Top Languages" width="55%" />\s*</div>\s*<br/>\s*'
new_content = re.sub(pattern, '', content)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Removed Top Languages section successfully")
