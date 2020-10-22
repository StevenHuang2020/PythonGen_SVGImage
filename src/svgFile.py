#Python3 Steven 
#Update: add lxml verion 09/07/2020 
import os
from lxml import etree
from svgBasic import *

#--------globla variables--------------#
gImageOutputPath = r'..\images'
#--------------------------------------#


class SVGFileV2:
    """SVGFileV2 xml version"""
    def __init__(self,fileName,W=100,H=100,border=False):
        self._initFile(fileName)
        self.fileName = fileName
        self.width = W
        self.height = H
        self.svgRoot = etree.Element("svg")
        self.svgRoot.set("width", str(self.width))
        self.svgRoot.set("height", str(self.height))
        self.svgRoot.set("xmlns", "http://www.w3.org/2000/svg")

        self.g = etree.SubElement(self.svgRoot, "g")
        self.g.set("opacity",'1.0')
        
        if border:
            self._addBorder()
            
    def _initFile(self,fileName):
        """remove svg file if already exist"""
        if os.path.exists(fileName):
            os.remove(fileName) 
            
    def svgSize(self):
        return self.width,self.height
    
    def _addBorder(self):
        rect = draw_rect(0, 0, self.width, self.height, stroke_width=1, \
            color='white',strokeColor='black')
        self.draw(rect)
                
    def setNodeAttri(self,node,attrbi,value):
        """set/add etree Element node attribute"""
        node.set(attrbi,str(value))
    
    def setNodeAttriDict(self,node,attrbiDict):
        for i in attrbiDict:
            self.setNodeAttri(node,i,attrbiDict[i])
        
    def draw(self, content):
        """link child to svgRoot child g element"""
        node = etree.fromstring(content)
        self.g.append(node)
        return node
    
    def close(self):
        """write lxml tree to file"""
        etree.ElementTree(self.svgRoot).write(self.fileName, pretty_print=True, \
            xml_declaration=True, encoding='UTF-8', standalone=False) 
        
        
class SVGFile:
    """SVGFile string io version,deprecated"""
    def __init__(self,fileName,W=100,H=100):
        self._initFile(fileName)
        self.fileName = fileName
        self.width = W
        self.height = H
        self._svgContent=''
        self._svgHeader()
        
    def _initFile(self,fileName):
        if os.path.exists(fileName):
            os.remove(fileName) 
    
    def _append2Svg(self,content):
        self._svgContent += content
        
    '''
    def _writeToFile(self,content):
        with open(self.fileName,'a',newline='\n') as dstF:
            dstF.write(content)   
            
    def _writeSVGHeader(self): 
        #<rect fill="#fff" stroke="#000" x="-70" y="-70" width="390" height="390"/> 
        header=[]
        s = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        header.append(s)
        s = f'<svg width="{self.width}" height="{self.height}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
        header.append(s)        
        s='    <g opacity="1.0">\n'
        header.append(s)
        
        for i in header:
            self._writeToFile(i)
                    
    def _writeSVGTail(self):
        tail = '    </g> \n</svg>'
        self._writeToFile(tail) 
    
    def draw(self, content):
        content = '        ' + content + '\n'
         self._writeToFile(content)
    '''
    
    def _writeToSvg(self):
        with open(self.fileName,'a',newline='\n') as dstF:
            dstF.write(self._svgContent)   
            
    def _svgHeader(self): 
        header=''
        s = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        header += s
        s = f'<svg width="{self.width}" height="{self.height}" version="1.1" xmlns="http://www.w3.org/2000/svg">\n'
        header += s        
        s='    <g opacity="1.0">\n'
        header += s
        self._append2Svg(header)
        
    def _svgTail(self):
        tail = '    </g> \n</svg>'
        self._append2Svg(tail)
     
    def draw(self, content):
        content = '        ' + content + '\n'
        self._append2Svg(content)
        
    def close(self):
        self._svgTail()
        self._writeToSvg()