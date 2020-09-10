
from svgBasic import *
from svgFile import *

def drawText():
    def GeFile():
        file = r'.\res\hi.txt'
        with open(file, 'r') as f:
            return f.readlines()
    
    def insert(source_str, insert_str, pos):
        return source_str[:pos]+insert_str+source_str[pos:]

    file = gImageOutputPath + r'\Hi.svg'
    H,W=200,1600
    #str='Hello'
    
    svg = SVGFile(file,W,H)
    if 0:
        y0 = 15
        for i in range(10):
            svg.draw(draw_text(0,y0,'.    Hello     World!        1'))
            y0 += 12
    else:
        strs = GeFile()
        y0 = 15
        h=12
        for i in strs:
            i = '.'.join(i)#insert(i,'.',0)
            #print(i)
            svg.draw(draw_text(0,y0,i))
            y0+=h
    svg.close()
    
def main():
    drawText()

if __name__=='__main__':
    main()