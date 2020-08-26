import os

class SVGFile:
    def __init__(self,fileName,W=100,H=100):
        self._initFile(fileName)
        self.fileName = fileName
        self.width = W
        self.height = H
        self._writeSVGHeader()
        
    def _initFile(self,fileName):
        if os.path.exists(fileName):
            os.remove(fileName)
            
    def _writeToFile(self,content):
        with open(self.fileName,'a',newline='\n') as dstF:
            dstF.write(content)    
        
    def _writeSVGHeader(self): 
        #<rect fill="#fff" stroke="#000" x="-70" y="-70" width="390" height="390"/> 
        header=[]
        s = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        header.append(s)
        s = f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">\n'
        header.append(s)        
        s='        <g opacity="1.0">\n'
        header.append(s)
        
        for i in header:
            self._writeToFile(i)
            
    def _writeSVGTail(self):
        tail = '        </g> \n</svg>'
        self._writeToFile(tail) 
        
    def draw(self, content):
        self._writeToFile(content + '\n')
        
    def close(self):
        self._writeSVGTail()