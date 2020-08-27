#python3 SVG basic
import random
import matplotlib as mpl
import numpy as np 

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

def randomColor():
    chars = '0123456789ABCDEF'
    color = ['#']
    for _ in range(6):
        color.append(random.choice(chars))
    return ''.join(color)

def randomColor2():
    #colors = ['#3300FF','#3366FF','#3399FF','#33FFFF','#CC6633']
    colors = ['#006600','#009933','#00CC66','#00FFCC','#6699FF']
    return random.choice(colors)

def randomColor3(i):
    N = 255 #number of grade colors
    #i = random.choice(range(N))
    try:
        return colorFader('k','w',i/N)
    except:
        print('i,i/n = ',i,i/N)
        
def draw_line(x, y, x2, y2, color='black'):
    #Draw a line for svg
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" />'

def draw_rect(x, y, width, height, color=None):
    #Draw a rectangle for svg
    color = color or randomColor()
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}"  fill="{color}" stroke="{color}" stroke_width="0.5"  />'

def draw_circle(x, y, radius, color='black'):
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{color}" />'

def draw_circleRings(x, y, radius, rings=5, color=None, fillColor='white'):
    #Draw circles rings for svg
    for _ in range(rings):
        r = random.randint(1,rings)*radius/(rings+1)
        sw = random.choice([1,1,1,2,2,3])
        color = color or randomColor()
        yield f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="{sw}" stroke="{color}" fill="none" />'
            
def draw_text(x,y,text,font='Consolas',color='black'):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="smaller" font-style="normal" font-variant="normal">{text}</text>'

def draw_path(path, width=30, color='black',fillColor='transparent'):
    #https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
    #M 100 306 C 168 444, 304 444, 352 306
    return f'<path d="{path}" stroke="{color}" stroke-width="{width}" fill="{fillColor}"/>'