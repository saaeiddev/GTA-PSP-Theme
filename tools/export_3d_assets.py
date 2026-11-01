#!/usr/bin/env python3
"""Split generated 3D icon atlases into PSP-sized transparent sources."""
from pathlib import Path
from PIL import Image,ImageOps
R=Path(__file__).resolve().parents[1]; P=R/'assets/icons'; A=R/'artwork/3d'
def split(im,columns,rows):
 w,h=im.size; output=[]
 for row in range(rows):
  for col in range(columns):
   # Sheet boundaries are integer-rounded; threshold the alpha to disregard stray low-alpha noise.
   box=(round(col*w/columns),round(row*h/rows),round((col+1)*w/columns),round((row+1)*h/rows))
   cell=im.crop(box).convert('RGBA'); alpha=cell.getchannel('A'); bb=alpha.point(lambda a: 255 if a>24 else 0).getbbox()
   if not bb: raise ValueError('empty atlas cell '+str((row,col)))
   output.append(cell.crop(bb))
 return output
def fit(im,size,margin=2):
 im=im.copy();im.thumbnail((size[0]-2*margin,size[1]-2*margin),Image.Resampling.LANCZOS)
 canvas=Image.new('RGBA',size);canvas.alpha_composite(im,((size[0]-im.width)//2,(size[1]-im.height)//2));return canvas
cat=split(Image.open(A/'category-atlas.png'),4,2); sub=split(Image.open(A/'submenu-atlas.png'),4,4)
for name,index in {'settings':0,'photo':1,'music':2,'video':3,'tv':6,'game':4,'network':5,'extras':7}.items(): fit(cat[index],(64,48)).save(P/'category'/f'{name}.png')
# Slots reuse related 3D assets where one sheet image represents several menu functions.
indices={2:0,4:1,6:2,8:3,10:4,12:5,14:5,16:6,18:7,20:2,22:8,24:9,26:10,28:11,30:'tv',32:12,34:13,36:15,38:15,40:14,42:3,44:'music',46:15,48:'network',50:14,52:13,54:'game',56:15,58:'music'}
catindices={'tv':6,'game':4,'network':5,'music':2}
for i,source in indices.items():
 files=list((P/'first-level').glob(f'{i:02d}-*.png'))
 if len(files)!=1:raise RuntimeError(f'slot {i} ambiguous')
 fit(cat[catindices[source]] if isinstance(source,str) else sub[source],(48,48)).save(files[0])
for i,src in [(0,sub[9]),(2,cat[5])]:
 files=list((P/'second-level').glob(f'{i:02d}-*.png'))
 if len(files)!=1:raise RuntimeError(f'slot {i} ambiguous')
 fit(src,(32,32)).save(files[0])
w=ImageOps.fit(Image.open(A/'wallpaper-master.png').convert('RGB'),(480,272),Image.Resampling.LANCZOS)
w.save(R/'assets/wallpaper.png');w.save(R/'assets/wallpaper-480x272.bmp')
print('Exported 3D-rendered category and submenu assets')
