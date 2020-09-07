
#Python3 Steven 09/07/2020 
# #svg file lxml version
import os
from lxml import etree
from svgBasic import *

class SVGFileV2:
    def __init__(self,fileName,W=100,H=100):
        self._initFile(fileName)
        self.fileName = fileName
        self.svgRoot = etree.Element("svg")
        self.svgRoot.set("width", str(W))
        self.svgRoot.set("height", str(H))
        self.svgRoot.set("xmlns", "http://www.w3.org/2000/svg")

        self.g = etree.SubElement(self.svgRoot, "g")
        self.g.set("opacity",'1.0')
        
    def _initFile(self,fileName):
        """remove svg file if already exist"""
        if os.path.exists(fileName):
            os.remove(fileName) 
     
    def draw(self, content):
        """link child to svgRoot child g element"""
        self.g.append(etree.fromstring(content))
        
    def close(self):
        """write lxml tree to file"""
        etree.ElementTree(self.svgRoot).write(self.fileName, pretty_print=True, \
            xml_declaration=True, encoding='UTF-8', standalone=False) 
    
def main():
    file=r'.\res\output.svg'
    svg = SVGFileV2(file)
    svg.draw(draw_line(0,0,100,100))
    svg.draw(draw_circle(50,50,20))
    svg.close()
    
if __name__=='__main__':
    main()
    