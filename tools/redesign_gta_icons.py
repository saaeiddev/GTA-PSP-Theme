#!/usr/bin/env python3
"""Original XMB pictograms with GTA-inspired outlined typography and radar framing."""
from pathlib import Path
import subprocess, re
from PIL import Image
R=Path(__file__).resolve().parents[1]
A=R/'artwork/icons'; P=R/'assets/icons'
B='#0c0e10'; W='#f5f6ed'; G='#9ad36a'; Y='#f0c94f'; RED='#ed6a54'
# Thick black strokes + white keylines are intentional, like the series' menu graphics.
def svg(body):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="480" viewBox="0 0 64 48"><g stroke="{B}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" paint-order="stroke fill">{body}</g></svg>'''
icons={
'settings':f'''<path fill="{W}" d="M9 25L32 8l23 17v18H9z"/><path fill="{B}" d="M15 26h34v15H15z"/><path fill="none" stroke="{W}" stroke-width="2" d="M18 29h28M18 34h28M18 39h28"/><path fill="{G}" d="M35 14c-3-4-3-8 1-10l3 5 4 1 4-4c2 4 1 7-3 9l-12 18-5-3z"/>''',
'photo':f'''<path fill="{W}" d="M10 14h11l3-5h14l3 5h12v27H10z"/><path fill="{B}" d="M13 19h38v16H13z"/><circle fill="{W}" cx="32" cy="27" r="11"/><circle fill="{B}" cx="32" cy="27" r="7"/><circle fill="{G}" cx="32" cy="27" r="3"/><circle fill="{RED}" cx="47" cy="17" r="2"/>''',
'music':f'''<path fill="none" stroke="{W}" stroke-width="3" d="M14 16L45 5"/><path fill="{W}" d="M9 15h46v28H9z"/><path fill="{B}" d="M12 18h40v22H12z"/><circle fill="{W}" cx="23" cy="29" r="9"/><circle fill="{B}" cx="23" cy="29" r="4"/><path fill="{G}" d="M36 21h12v5H36z"/><path fill="none" stroke="{W}" stroke-width="2" d="M36 30h12M36 34h9"/>''',
'video':f'''<path fill="{W}" d="M10 15h44v27H10z"/><path fill="{B}" d="M12 23h40v17H12z"/><path fill="{W}" d="M10 14l42-8 2 8-42 8z"/><path fill="{B}" d="M15 13l5-1 5 5-5 1zM28 10l5-1 5 5-5 1zM41 8l5-1 4 5-5 1z"/><path fill="{G}" d="M29 25l11 7-11 6z"/>''',
'tv':f'''<path fill="none" stroke="{W}" stroke-width="3" d="M22 9l-5-5M40 9l6-5"/><rect fill="{W}" x="9" y="10" width="46" height="33" rx="4"/><rect fill="{B}" x="13" y="14" width="30" height="24" rx="2"/><path fill="{G}" d="M17 32l7-8 6 4 5-7 5 12H17z"/><circle fill="{Y}" cx="49" cy="20" r="2"/><circle fill="{W}" cx="49" cy="30" r="2"/>''',
'game':f'''<g font-family="DejaVu Sans" font-weight="900" fill="{W}" stroke="{B}" stroke-width="2.4" paint-order="stroke fill" letter-spacing="-1.4"><text x="8" y="14" font-size="13">grand</text><text x="8" y="27" font-size="13">theft</text><text x="8" y="40" font-size="17">auto</text></g><path fill="{G}" d="M51 19l2.3 4.8 5.2.6-3.8 3.6 1 5-4.7-2.5-4.7 2.5 1-5-3.8-3.6 5.2-.6z"/>''',
'network':f'''<circle fill="{W}" cx="32" cy="24" r="20"/><circle fill="{B}" cx="32" cy="24" r="16"/><path fill="none" stroke="{W}" stroke-width="2" d="M18 18l11 5 5-8 10 3M20 31l10-4 8 7 8-6M27 9l3 18-2 12"/><path fill="{G}" d="M32 16l7 14-7-3-7 3z"/><circle fill="{Y}" cx="43" cy="17" r="2.3"/>''',
'extras':f'''<path fill="{W}" d="M32 3l5.8 12 13.4 1.8-9.7 9.2 2.5 13.2L32 33l-12 6.2 2.5-13.2-9.7-9.2L26.2 15z"/><path fill="{B}" d="M32 11l3.5 7.2 8 .9-5.8 5.6 1.5 7.8-7.2-3.8-7.2 3.8 1.5-7.8-5.8-5.6 8-.9z"/><path fill="{Y}" d="M32 17l2 4.2 4.6.6-3.3 3.2.8 4.5-4.1-2.1-4.1 2.1.8-4.5-3.3-3.2 4.6-.6z"/>'''
}
for name,body in icons.items(): (A/'category'/f'{name}.svg').write_text(svg(body))
# Preserve each item's semantic pictogram, redraw inside a white outlined radar disk.
subprocess.run(['python3',str(R/'tools/create_first_level_icons.py')],check=True)
for f in sorted((A/'first-level').glob('*.svg')):
 s=f.read_text(); inner=re.search(r'(<g [^>]+>.*</g>)</svg>',s).group(1)
 # Original artwork is an editable group nested inside an intentionally dark GTA-map HUD disc.
 inner=inner.replace('#3d995f',G).replace('#c95b50',RED).replace('#f8f6eb',W).replace('#e9b94c',Y)
 star=f'<path d="M38 4l1.6 3.3 3.6.5-2.6 2.5.6 3.5-3.2-1.7-3.2 1.7.6-3.5-2.6-2.5 3.6-.5z" fill="{Y}" stroke="{B}" stroke-width="1"/>'
 frame=f'<circle cx="24" cy="24" r="22" fill="{B}" stroke="{W}" stroke-width="2.5"/><path d="M6 29l11-6 10 6 12-7M12 9l7 10-2 19" fill="none" stroke="#425f48" stroke-width="1.2"/>'
 f.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="480" height="480" viewBox="0 0 48 48">{frame}<g transform="translate(7 7) scale(.70)">{inner}</g>{star}</svg>')
for folder,sz in [('category',(64,48)),('first-level',(48,48))]:
 for src in sorted((A/folder).glob('*.svg')):
  out=P/folder/(src.stem+'.png')
  subprocess.run(['inkscape',str(src),'--export-filename='+str(out),'--export-width='+str(sz[0]),'--export-height='+str(sz[1])],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
for n,src in [('00-wallpaper','24-theme-settings'),('02-color','54-fallback')]:
 Image.open(P/'first-level'/f'{src}.png').resize((32,32),Image.Resampling.LANCZOS).save(P/'second-level'/f'{n}.png')
print('Exported 8 redesigned category icons and 29 radar-framed icons')
