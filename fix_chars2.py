path = r'c:\Users\LENOVO\Desktop\web\New folder (2)\gpt\4thsection.html'

# Read as raw bytes to see what's actually there
with open(path, 'rb') as f:
    raw = f.read()

# These are the mojibake sequences (UTF-8 bytes misread as latin-1)
# and their correct UTF-8 replacements
fixes = [
    (b'\xe2\x9c\xa6', '\u2726'.encode('utf-8')),   # âœ¦ -> ✦
    (b'\xef\xbc\x8b', b'+'),                         # ï¼‹ -> +
    (b'\xe2\x9c\x94', '\u2714'.encode('utf-8')),   # âœ" -> ✔
    (b'\xe2\x99\xa1', '\u2661'.encode('utf-8')),   # â™¡ -> ♡
    (b'\xc3\x97',     '\u00d7'.encode('utf-8')),   # Ã— -> ×
    (b'\xe2\x86\x92', '\u2192'.encode('utf-8')),   # â†' -> →
    (b'\xe2\x88\x92', '\u2212'.encode('utf-8')),   # âˆ' -> −
    (b'\xe2\x9c\xb3', '\u2733'.encode('utf-8')),   # âœ³ -> ✳
    (b'\xf0\x9f\x9b\x92', '\U0001F6D2'.encode('utf-8')), # shopping cart emoji (keep as-is but clean)
]

for bad_bytes, good_bytes in fixes:
    count = raw.count(bad_bytes)
    print(f'Replacing {bad_bytes!r}: {count} occurrences')
    raw = raw.replace(bad_bytes, good_bytes)

with open(path, 'wb') as f:
    f.write(raw)

print('Done')
