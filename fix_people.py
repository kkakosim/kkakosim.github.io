import re

with open('_pages/people.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Move Lazaros Zarras to alumni Post-Graduate
content = re.sub(r'\s*<li>Lazaros Zarras: MSc studies at Hanze University of Applied Sciences, Netherlands</li>', '', content)
# Add him to alumni Post-Graduate
content = content.replace('<h2 class="category">alumni Post-Graduate</h2>\n    <ol>', '<h2 class="category">alumni Post-Graduate</h2>\n    <ol>\n        <li>Lazaros Zarras: MSc studies at Hanze University of Applied Sciences, Netherlands</li>')

# 2. Move alumni Undergraduate before alumni Doctorate and change to <ol>
undergrad_alumni_section = re.search(r'(<a id="undergraduate-alumni" href="\.#undergraduate-alumni">\s*<h2 class="category">alumni Undergraduate</h2>\s*</a>\s*)<ul>(.*?)</ul>', content, re.DOTALL)

if undergrad_alumni_section:
    full_match = undergrad_alumni_section.group(0)
    # Change ul to ol
    new_undergrad = undergrad_alumni_section.group(1) + "<ol>" + undergrad_alumni_section.group(2) + "</ol>"
    
    # Remove from original location
    content = content.replace(full_match, '')
    
    # Insert before alumni Doctorate
    content = content.replace('<a id="doctorate"', new_undergrad + '\n    <a id="doctorate"')

with open('_pages/people.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
