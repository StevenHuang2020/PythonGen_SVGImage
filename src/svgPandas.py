#python3 Steven 11/06/20 Auckland,NZ

import numpy as np
import pandas as pd 
from svgBasic import *
from svgFile import *
from svgFunction import *
from common import gImageOutputPath
from geoTransformation import *
from svgSmile import drawSmileSVGNode

def getDataSet():
    #return pd.DataFrame(np.arange(12).reshape(-1, 3), columns=['A', 'B', 'C'])
    #return pd.DataFrame(np.random.randint(1,150, size=(5,3)), columns=['A', 'B', 'C'])
    
    data = {'Name':['Tom', 'Jane', 'Steve', 'Ricky'], 'Gender':['Male','Female','Male','Male'], 'Age':[28,34,29,42]}
    return pd.DataFrame(data)

def plotTableBorder(svg, node, df):
    W,H = svg.getSize()
    print('df.shape=',df.shape)
    indexs = df.index
    columns = df.columns
    print('indexs=',indexs)
    print('columns=',columns)
    print(df)
    row,col = df.shape
    
    offsetX = 5
    offsetY = 5
    colWidth = (W-2*offsetX)/(col+1) #45
    rowHeight = (H-2*offsetY)/(row+1) #25
    
    styleDict={}
    styleDict['stroke'] = 'black' 
    styleDict['stroke-width'] = '0.5'
    svg.drawNode(node, add_style('line', getStyleList(styleDict)))

    anyDict={}
    #anyDict['stroke'] = 'black'
    #anyDict['stroke-width'] = 0.5
    for i in range(row+2):
        x1 = offsetX
        y1 = offsetY + i*rowHeight
        x2 = x1 + (col+1)*colWidth
        y2 = y1
        
        anyDict['x1'] = x1
        anyDict['y1'] = y1
        anyDict['x2'] = x2
        anyDict['y2'] = y2
        svg.drawNode(node, draw_any('line', **anyDict))
    
    for i in range(col+2):
        x1 = offsetX + i*colWidth
        y1 = offsetY
        x2 = x1 
        y2 = y1 + (row+1)*rowHeight
        
        anyDict['x1'] = x1
        anyDict['y1'] = y1
        anyDict['x2'] = x2
        anyDict['y2'] = y2
        svg.drawNode(node, draw_any('line', **anyDict))

    styleDict={}
    #styleDict['fill'] = 'black' 
    styleDict['font-family'] = 'Consolas'
    #styleDict['font-size'] = '22px'
    styleDict['dominant-baseline'] = "middle"
    styleDict['text-anchor'] = "middle"
        
    svg.drawNode(node, add_style('text', getStyleList(styleDict)))
    
    anyDict={}
    anyDict['font-size'] = '14px'
    anyDict['fill'] = 'red'
    """draw index text"""
    for i,index in enumerate(indexs):
        #print(index)
        x1 = offsetX
        y1 = offsetY + (i+1)*rowHeight
        x = x1 + colWidth/2
        y = y1 + rowHeight/2
        
        anyDict['x'] = x
        anyDict['y'] = y
        svg.drawNode(node, draw_any('text', index, **anyDict))
        
    """draw column text"""    
    for i,column in enumerate(columns):
        #print(column)
        x1 = offsetX + (i+1)*colWidth
        y1 = offsetY 
        x = x1 + colWidth/2
        y = y1 + rowHeight/2
        
        anyDict['x'] = x
        anyDict['y'] = y
        svg.drawNode(node, draw_any('text', column, **anyDict))
        
    """draw content text"""
    for i in range(row):
        for j in range(col):
            x = offsetX + (j+1)*colWidth
            y = offsetY + (i+1)*rowHeight
            
            if 1:#style1
                anyDict['x'] = x + colWidth/2
                anyDict['y'] = y + rowHeight/2
                anyDict['font-size'] = '12px'
                anyDict['fill'] = 'black'
                svg.drawNode(node, draw_any('text', df.iloc[i,j], **anyDict))
            elif 0:
                anyDict['x'] = x
                anyDict['y'] = y
                anyDict['width'] = colWidth
                anyDict['height'] = rowHeight
                
                maxV  = np.max(df.values)
                minV  = np.min(df.values)
                scalar = (df.iloc[i,j] - minV)/(maxV-minV)
                anyDict['fill'] =  colorFader('#C0392B', '#3498DB', scalar)#'blue'
                svg.drawNode(node, draw_any('rect', df.iloc[i,j], **anyDict))
            elif 1:
                r = rowHeight//2-1
                x = x + colWidth/2 - r
                y = y + rowHeight/2 -r 
                drawSmileSVGNode(svg, node, radius=r, offsetX=x, offsetY=y)
                #svg.drawNode(node, draw_any('rect', df.iloc[i,j], **anyDict))
                #svg.drawNode(node, draw_any('circle', cx=x,cy=y,r=2,fill='red'))
                
def plotTable(svg, node, df):
    print('df=\n',df)
    indexs = df.index
    columns = df.columns
    print('indexs=',indexs)
    print('columns=',columns)
         
def drawDataFrame(svg):
    H,W = svg.getSize()
    cx,cy = W//2,H//2
    svg.setTitle('draw Datafrane data')

    g = svg.draw(draw_any('g', opacity=1.0))
    #anyNode = svg.drawNode(g, draw_any('test','222', a=10, b="4",c='red',xml='www.ss'))
    #svg.drawNode(g, draw_any('test','hello'))
    df = getDataSet()
    plotTableBorder(svg, g, df)
    #plotTable(svg, g, df)
    '''
    anyDict={}
    anyDict['test'] = 1
    anyDict['xml'] = 'www.ggg'
    anyDict['a'] = 'aaaaa anything else'
    anyDict['b'] = 'red black xxxxxxxxxxxxxxxxx anything you want'
    svg.drawNode(g, draw_any('test2', **anyDict))
    svg.drawNode(g, draw_any('hello', **anyDict))
    svg.drawNode(g, draw_any('anything', **anyDict))
    
    for i in range(20):
        anyDict={}
        anyDict['cx'] = cx
        anyDict['cy'] = cy
        anyDict['r'] = '5'
        anyDict['stroke'] = '#80ff00'
        anyDict['stroke-width'] = '2'
        anyDict['fill'] = 'none'
        
        circle = svg.drawNode(g, draw_any('circle', **anyDict))
        #'from' is a key word of python for import libs, but here last resort change parameter 
        # from(attribute of animate element for svg) to 'From' to avoid conflict.
        svg.drawNode(circle, draw_any('animate', fill='freeze', attributeName='r', From="5", to="80", dur="4s", begin=str(i), repeatCount="indefinite"))
        
        anyDict={}       
        anyDict['attributeName'] = 'stroke-width'
        anyDict['values'] = '1;2;3;2;1'
        anyDict.pop("from", None)
        anyDict.pop("to", None)
        svg.drawNode(circle, draw_any('animate', **anyDict))
        
        anyDict['attributeName'] = 'stroke'
        anyDict['from'] = '#80ff00'
        anyDict['to'] = '#0000ff'
        anyDict['begin'] = '1s'
        anyDict.pop("values", None)
        svg.drawNode(circle, draw_any('animate', **anyDict))
    '''
    
def main():
    file = gImageOutputPath + r'\dataFrame.svg'
    H,W=120,200
    svg = SVGFileV2(file,W,H,border=True)
    drawDataFrame(svg)
    svg.close()
    
if __name__ == '__main__':
    main()
