#python3 SVG basic
import random

def randomColor():
    chars = '0123456789ABCDEF'
    color = ['#']
    for i in range(6):
        color.append(random.choice(chars))
    return ''.join(color)

def draw_line(x, y, x2, y2, color='black'):
    #Draw a line for svg
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" />'

def draw_rect(x, y, width, height, color=None):
    #Draw a rectangle for svg
    color = color or randomColor()
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" \
        fill="{color}" stroke="{color}" stroke_width="0.5"  />'

def draw_circle(x, y, radius, rings=3, color='black'):
    #Draw circles for svg
    for _ in range(rings):
        r = random.randint(1,rings)*radius/(rings+1)
        sw = random.choice([1,1,1,2,2,3])
        yield f'<circle cx="{x}" cy="{y}" r="{r}" stroke_width="{sw}" \
            fill="{color}" />'

def draw_circleRings(x, y, radius, rings=5, color=None, fillColor='white'):
    #Draw circles rings for svg
    for _ in range(rings):
        r = random.randint(1,rings)*radius/(rings+1)
        sw = random.choice([1,1,1,2,2,3])
        color = color or randomColor()
        yield f'<circle cx="{x}" cy="{y}" r="{r}" stroke_width="{sw}" \
            stroke="{color}" fill="{fillColor}" />'
            