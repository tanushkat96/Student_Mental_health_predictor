from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

assets = Path('assets')
assets.mkdir(exist_ok=True)

try:
    font = ImageFont.truetype('arial.ttf', 20)
except IOError:
    font = ImageFont.load_default()


def draw_box(draw, xy, text, fill='#ffffff', outline='#000000'):
    draw.rectangle(xy, fill=fill, outline=outline, width=2)
    x1, y1, x2, y2 = xy
    lines = text.split('\n')
    total_h = sum(draw.textbbox((0, 0), line, font=font)[3] for line in lines)
    y = y1 + (y2 - y1 - total_h) / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        draw.text((x1 + (x2-x1-w)/2, y), line, fill='black', font=font)
        y += h

# Flowchart
w, h = 1200, 900
img = Image.new('RGB', (w, h), 'white')
d = ImageDraw.Draw(img)

boxes = [
    ((100, 70, 400, 170), 'User Input\nStreamlit UI'),
    ((100, 240, 400, 340), 'Input Preprocessing\n(feature encode, scale)'),
    ((100, 410, 400, 510), 'Prediction Engine\nRandom Forest Model'),
    ((100, 580, 400, 680), 'Result Display\nRisk Output + Insights'),
    ((650, 240, 1000, 340), 'Analytics Dashboard\nVisualizations + Stats'),
    ((650, 580, 1000, 680), 'Resource Page\nWellness Links + Tips'),
]
for xy, text in boxes:
    draw_box(d, xy, text)

arrow_lines = [((250, 170), (250, 240)), ((250, 340), (250, 410)), ((250, 510), (250, 580)),
               ((400, 280), (650, 280)), ((650, 510), (650, 580))]
for start, end in arrow_lines:
    d.line([start, end], fill='black', width=4)
    dx, dy = end[0]-start[0], end[1]-start[1]
    if abs(dx) > abs(dy):
        sign = 1 if dx > 0 else -1
        arrow = [(end[0]-sign*20, end[1]-10), end, (end[0]-sign*20, end[1]+10)]
    else:
        sign = 1 if dy > 0 else -1
        arrow = [(end[0]-10, end[1]-sign*20), end, (end[0]+10, end[1]-sign*20)]
    d.line(arrow, fill='black', width=4)

d.text((360, 10), 'Application Flow Diagram', fill='black', font=font)
img.save(assets / 'flowchart.png')

# Architecture diagram
img = Image.new('RGB', (w, h), 'white')
d = ImageDraw.Draw(img)
layer_boxes = [
    ((150, 120, 400, 220), 'User Interface\nStreamlit Frontend'),
    ((150, 270, 400, 370), 'Application Layer\nInput Validation\nPrediction Logic'),
    ((150, 420, 400, 520), 'Model Layer\nRandom Forest + Features'),
    ((150, 570, 400, 670), 'Data Layer\nCSV Dataset + Pickle Models'),
    ((700, 200, 1050, 300), 'Analytics + Charts\nMatplotlib / Seaborn'),
    ((700, 360, 1050, 460), 'Resources Page\nLinks, Tips, Videos'),
    ((700, 520, 1050, 620), 'Assets / Styling\nCSS + Images'),
]
for xy, text in layer_boxes:
    draw_box(d, xy, text, fill='#eef6ff')

arrows = [((275, 220), (275, 270)), ((275, 370), (275, 420)), ((275, 520), (275, 570)),
          ((400, 145), (700, 245)), ((400, 320), (700, 320)), ((400, 495), (700, 540))]
for start, end in arrows:
    d.line([start, end], fill='black', width=4)
    dx, dy = end[0]-start[0], end[1]-start[1]
    if abs(dx) > abs(dy):
        sign = 1 if dx > 0 else -1
        arrow = [(end[0]-sign*20, end[1]-10), end, (end[0]-sign*20, end[1]+10)]
    else:
        sign = 1 if dy > 0 else -1
        arrow = [(end[0]-10, end[1]-sign*20), end, (end[0]+10, end[1]-sign*20)]
    d.line(arrow, fill='black', width=4)

d.text((340, 20), 'System Architecture Diagram', fill='black', font=font)
img.save(assets / 'architecture.png')

print('created diagrams')
