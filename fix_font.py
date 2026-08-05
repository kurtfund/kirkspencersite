import os
import re

base_dir = '/Users/kirkspencer/Documents/kirkspencersite'
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add Google Fonts to index.html if not present
if 'fonts.googleapis.com' not in html:
    fonts = """<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700&display=swap" rel="stylesheet"/>"""
    html = html.replace('</head>', fonts + '\n</head>')

# Add CSS to force Inter
force_font = """<style>
  body, html, * {
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif !important;
  }
</style>"""
if 'force_font' not in html:
    html = html.replace('</head>', force_font + '\n</head>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Font updated in index.html")
