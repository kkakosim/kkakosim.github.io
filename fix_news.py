import os
import re

news_dir = '_news'

def update_file(filename, new_filename, new_date):
    filepath = os.path.join(news_dir, filename)
    if not os.path.exists(filepath): return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if new_date:
        content = re.sub(r'date: 2026-\d{2}-\d{2}', f'date: {new_date}', content)
    
    # Add inline style for max-width to make them small thumbnails
    content = content.replace('class="img-fluid rounded z-depth-1"', 'class="img-fluid rounded z-depth-1" style="max-width: 250px;"')
    
    new_filepath = os.path.join(news_dir, new_filename)
    with open(new_filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
        
    if filepath != new_filepath:
        os.remove(filepath)

# Update Linke (was 20260810, now 20260508)
update_file('20260810.md', '20260508.md', '2026-05-08')

# Update Economou (was 20260820, now 20260326)
update_file('20260820.md', '20260326.md', '2026-03-26')

# Update Ioannidou/Karathanasi (was 20260715, now 20260713)
update_file('20260715.md', '20260713.md', '2026-07-13')

# Update the rest just for the thumbnail
update_file('20260515.md', '20260515.md', None)
update_file('20260929.md', '20260929.md', None)

# Add COST Action CA25146 news post
cost_news = '''---
layout: post
date: 2026-09-30 10:00:00+0300
inline: true
related_posts: false
---
Awarded new EU COST Action CA25146 - "Sustainable Aerosol and Particle Technology for Industrial Applications Network (SPARTAN)".
'''
with open(os.path.join(news_dir, '20260930_cost.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(cost_news)

