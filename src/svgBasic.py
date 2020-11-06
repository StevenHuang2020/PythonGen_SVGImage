#python3 SVG basic
import random
import matplotlib as mpl
import numpy as np 
import string

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

def randomColor():
    """web hex color format"""
    chars = '0123456789ABCDEF'
    return '#' + ''.join(random.sample(chars,6))
    
def randomColor2():
    #colors = ['#3300FF','#3366FF','#3399FF','#33FFFF','#CC6633']
    colors = ['#006600','#009933','#00CC66','#00FFCC','#6699FF']
    return random.choice(colors)

def randomColor3(i,N=255):
    #N: number of grade colors
    #i = random.choice(range(N))
    try:
        return colorFader('k','w',i/N)
    except:
        print('i,i/n = ',i,i/N)

def convertRGB(rgb): #covert from rgb to hex color
    def clip(x): 
        return max(0, min(x, 255))
    return "#{0:02x}{1:02x}{2:02x}".format(rgb[0], rgb[1], rgb[2])

def clipFloat(x, n=1):
    if isinstance(x,float):
        return round(x, n)
    return x

def ranstr(num): #random string as ID
    return ''.join(random.sample(string.ascii_letters + string.digits, num))
    
def getStyleList(styleDict):
    styleList=''
    for key, value in styleDict.items():
        styleList = styleList + (key + ': ' + str(value) + '; ')
    return styleList

#------------------------------draw function---------------------------------#        
def draw_line(x, y, x2, y2, stroke_width=0.5, color='black'):
    #Draw a line for svg
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{stroke_width}"/>'

def draw_rect(x, y, width, height, stroke_width=0.5, color=None, strokeColor=None):
    #Draw a rectangle for svg
    color = color or randomColor()
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}"  fill="{color}" stroke="{strokeColor}" stroke-width="{stroke_width}"  />'

def draw_circle(x, y, radius, color='black'):
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{color}" />'

def draw_circleRings(x, y, radius, rings=5, color=None, fillColor='white'):
    #Draw circles rings for svg
    for _ in range(rings):
        r = random.randint(1,rings)*radius/(rings+1)
        sw = random.choice([1,1,1,2,2,3])
        color = color or randomColor()
        yield f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="{sw}" stroke="{color}" fill="none" />'
            
def draw_text(x,y,text,font='Consolas',fontsize='smaller',color='black',blankSpace='pre'):
    #return f'<text x="{x}" y="{y}" fill="{color}" xml:space="{blankSpace}" font-family="{font}" font-size="{fontsize}" font-style="normal" font-variant="normal">{text}</text>'
    #xml:space deprecated.   white-space: normal,pre,nowrap,pre-wrap,break-spaces,pre-line
    return f'<text x="{x}" y="{y}" fill="{color}" white-space="{blankSpace}" font-family="{font}" font-size="{fontsize}" font-style="normal" font-variant="normal">{text}</text>'

def draw_text_only(x,y,text):
    return f'<text x="{x}" y="{y}" >{text}</text>'

def draw_path(path, width=30, color='black',fillColor='transparent'):
    #https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths
    #M 100 306 C 168 444, 304 444, 352 306
    return f'<path d="{path}" stroke="{color}" stroke-width="{width}" fill="{fillColor}" />'

def add_style(tag,styleList):
    return '<style> %s { %s } </style>' % (tag,styleList)

def add_style_path(stroke='black', stroke_width=1, fill='transparent'):
    style = f'stroke: {stroke}; stroke-width: {stroke_width}; fill: {fill};'
    return add_style(tag='path', styleList = style)
   
def draw_Only_path(path):
    return f'<path d="{path}"/>'

def draw_polygon(points, color=None, strokeColor=None, stroke_width=1.0):
    return f'<polygon points="{points}" stroke="{strokeColor}" stroke-width="{stroke_width}" fill="{color}" />'
 
def draw_tag(tag, text=None):
    return draw_any(tag, text)

def draw_any(tag, text=None, **kwargs): 
    """draw_any(tagName, text, attr1=anything, attr2=anything, ...) or draw_any(tagName, text, **attrDict)"""
    attriList = ' '.join([(str(key) + '=' + '"' + str(value) + '"') for key, value in kwargs.items()])
    #print('attriList=',attriList)
    if text is not None:
        return "<{} {}>{}</{}>".format(tag, attriList,text,tag)
    return "<{} {} />".format(tag, attriList)
