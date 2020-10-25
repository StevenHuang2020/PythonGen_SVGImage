#python3 Steven Scalable Vector Graphics(SVG)
#reference: https://en.wikipedia.org/wiki/Scalable_Vector_Graphics
#SVG: https://www.w3.org/Graphics/SVG/
import os
import numpy as np 
import random
from svgBasic import *
from svgFile import *
from svgImageMask import maskImage
from svgSmile import testSmile
from svgFunction import *
from svgDrawArt import drawArtSvg
from svgRandomPath import drawRandomPath, drawRandomCirclePath
from svgRandomPath import drawRandomRectanglePath, drawHearCurve
from svgRandomWalk import drawRandomNumbersPath, drawRandomWalkPath
from svgLineGraph import drawLineGraphic
from svgText import drawText
from common import gImageOutputPath

def drawTest():
    file=gImageOutputPath + r'\test.svg'
    H,W=100,100
    svg = SVGFile(file,W,H)
    svg.draw(draw_line(0,0,100,100))
    svg.close()
            
def main():
    # drawTest()
    # drawArtSvg()
    # drawText()
    # maskImage()
    # testSmile()
    # drawHearCurve()
    # drawRandomPath()
    # drawRandomCirclePath()
    # drawRandomRectanglePath()
    # drawRandomNumbersPath()
    # drawRandomWalkPath()
    # drawLineGraphic()
    pass
    
if __name__=='__main__':
    main()