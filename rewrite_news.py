import os

files = {
    '20260326.md': {
        'text': 'Invited lecture by Prof. Ioannis G. Economou on "Multi-Scale Simulation of Complex Chemical Systems".',
        'img': 'economou_cover.jpg',
        'tmb': 'economou_cover_tmb.jpg'
    },
    '20260508.md': {
        'text': 'Invited lecture by Prof. Patrick Linke on "Systematic Innovation in Chemical Process Design".',
        'img': 'linke_media.png',
        'tmb': 'linke_media_tmb.png'
    },
    '20260515.md': {
        'text': 'Congratulations to George Pitsos for successfully defending his undergraduate thesis "Extension of evacuation models with dynamic pathfinding based on toxic load exposure".',
        'img': 'pitsos_defence_202604.jpg',
        'tmb': 'pitsos_defence_202604_tmb.jpg'
    },
    '20260713.md': {
        'text': 'Congratulations to Nikoleta Ioannidou and Paraskevi Karathanasi for successfully defending their undergraduate theses!',
        'img': 'nikoleta_paraskevi_defence_202607.jpg',
        'tmb': 'nikoleta_paraskevi_defence_202607_tmb.jpg'
    },
    '20260929.md': {
        'text': 'Nikoleta presented her work "Behavior of Particle Deposits on Pipelines under Wind Cross-Flow Conditions" at the APT conference.',
        'img': 'nikoleta_apt_presentation.jpg',
        'tmb': 'nikoleta_apt_presentation_tmb.jpg'
    }
}

for filename, data in files.items():
    filepath = os.path.join('_news', filename)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parts = content.split('---')
    if len(parts) >= 3:
        front_matter = parts[1]
    else:
        continue
        
    new_content = f'''---{front_matter}---
<div class="news-thumbnail" style="display: none;">
  <img src="{{{{ '/assets/img/{data['tmb']}' | relative_url }}}}" class="img-fluid rounded z-depth-1 float-right ml-3" style="max-width: 150px;" alt="thumbnail">
</div>
{data['text']}
<div class="news-full mt-3">
  <img src="{{{{ '/assets/img/{data['img']}' | relative_url }}}}" class="img-fluid rounded z-depth-1" style="max-height: 300px; width: auto;" alt="image">
</div>
'''
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(new_content)
