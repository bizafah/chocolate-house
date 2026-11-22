path = r'c:\Users\LENOVO\Desktop\web\New folder (2)\gpt\4thsection.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the benefit-icon section and show bytes around it
idx = content.find('benefit-icon')
snippet = content[idx:idx+200]
print('Text snippet:')
print(repr(snippet))
print()
print('Bytes:')
print(snippet.encode('utf-8').hex())
