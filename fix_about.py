import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace existing style block with the new one
new_style = '''<style>
  /* Show thumbnails and hide full images on the front page news section */
  .news .news-thumbnail {
    display: block !important;
  }
  .news .news-full {
    display: none !important;
  }
</style>'''

content = re.sub(r'<style>.*?Show thumbnails.*?<\/style>', new_style, content, flags=re.DOTALL)

with open('_pages/about.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
