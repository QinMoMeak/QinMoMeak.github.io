from pathlib import Path

img_dir = Path('./').resolve()

for index, img_path in enumerate(img_dir.glob('*.png')):
    sub = img_path.name.find('(')
    sub1 = img_path.name.find(')')
    name = img_path.with_name(f'{img_path.name[:sub-1]}{img_path.name[sub+1:sub1]}.png')
    img_path.rename(name)