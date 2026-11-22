path = r'c:\Users\LENOVO\Desktop\web\New folder (2)\gpt\4thsection.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '\u00e2\u009c\u00a6': '\u2726',   # âœ¦ -> ✦
    '\u00ef\u00bc\u008b': '+',          # ï¼‹ -> +
    '\u00e2\u009c\u0094': '\u2714',   # âœ" -> ✔
    '\u00e2\u0099\u00a1': '\u2661',   # â™¡ -> ♡
    '\u00c3\u0097': '\u00d7',          # Ã— -> ×
    '\u00e2\u0086\u0092': '\u2192',   # â†' -> →
    '\u00e2\u02c6\u0092': '\u2212',   # âˆ' -> −
    '\u00e2\u009c\u00b3': '\u2733',   # âœ³ -> ✳
}

for bad, good in replacements.items():
    content = content.replace(bad, good)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
