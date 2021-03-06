
from svgBasic import *
from svgFile import *
import re
import cProfile
from common import gImageOutputPath

def drawText():
    def GeFile():
        file = r'.\res\hi.txt'
        with open(file, 'r') as f:
            return f.readlines()

    file = gImageOutputPath + r'\Hi.svg'
    H,W=200,1200
    #str='Hello'
    
    svg = SVGFileV2(file,W,H,border=False)
    
    styleDict={}
    styleDict['fill'] = 'black' 
    styleDict['font-family'] = 'Consolas' 
    styleDict['font-size'] = '10px'
    styleDict['font-style'] = 'normal' 
    styleDict['font-variant'] = 'normal' 
    #styleDict['xml:space'] = 'preserve' #deprecated
    styleDict['white-space'] = 'pre'
        
    styleList = getStyleList(styleDict)
    svg.draw(add_style('text',styleList))
    
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
            #i = i.replace('#', '@')
            i = ' '.join(i)#'.'.join(i)
            print(i)
            #svg.draw(draw_text(0,y0,i, blankSpace='preserve'))
            text = svg.draw(draw_text_only(0,y0,i))
            
            #attr = "{{{}}}".format(svg.namespace) + 'space' #
            #svg.setNodeAttri(text, attr,"preserve") #error without namespace
            y0+=h
            
    svg.close()
    
'''
新細明體：PMingLiU 
細明體：MingLiU 
標楷體：DFKai-SB 
黑体：SimHei 
宋体：SimSun 
新宋体：NSimSun 
仿宋：FangSong 
楷体：KaiTi 
仿宋_GB2312：FangSong_GB2312 
楷体_GB2312：KaiTi_GB2312 
微軟正黑體：Microsoft JhengHei 
微软雅黑体：Microsoft YaHei 
隶书：LiSu 
幼圆：YouYuan 
华文细黑：STXihei 
华文楷体：STKaiti 
华文宋体：STSong 
华文中宋：STZhongsong 
华文仿宋：STFangsong 
方正舒体：FZShuTi 
方正姚体：FZYaoti 
华文彩云：STCaiyun 
华文琥珀：STHupo 
华文隶书：STLiti 
华文行楷：STXingkai 
华文新魏：STXinwei
'''

def drawPoet(svg):
    '''
    poet = []
    poet.append('感遇·其一')
    poet.append('张九龄')
    poet.append('兰叶春葳蕤，桂华秋皎洁。')
    poet.append('欣欣此生意，自尔为佳节。')
    poet.append('谁知林栖者，闻风坐相悦。')
    poet.append('草木有本心，何求美人折？')
    '''
    poet = []
    poet.append('過故人莊')
    poet.append('孟浩然')
    poet.append('故人具雞黍，邀我至田家。')
    poet.append('綠樹村邊合，青山郭外斜。')
    poet.append('開軒面場圃，把酒話桑麻。')
    poet.append('待到重陽日，还來就菊花。')

    styleDict={}
    styleDict['fill'] = 'red' 
    styleDict['font-family'] = 'KaiTi' #'Microsoft YaHei' 
    styleDict['font-size'] = '12px' 
    #font-style: normal; font-variant: normal;
    
    styleList = getStyleList(styleDict)
    
    W,H = svg.getSize()
    svg.draw(add_style('text',styleList)) 
        
    offsetx = 25
    offsety = 20
    x0 = W - 2*offsetx
    y0 = offsety
    yInter = 15 
    xInter = 25
    
    x = x0
    y = y0
    for i in poet:
        for c in i:
            svg.draw(draw_text_only(x,y,text=c))
            y = y + yInter
        y = y0
        x = x - xInter
        
def drawPoet2(svg):
    poet = []
    poet.append('紅樓夢')
    poet.append('可嘆停機德，')
    poet.append('堪憐詠絮才。')
    poet.append('玉帶林中掛，')
    poet.append('金簪雪裡埋。')

    styleDict={}
    styleDict['fill'] = 'red' 
    styleDict['font-family'] = 'Microsoft YaHei' 
    styleDict['font-size'] = '24px' 
    #font-style: normal; font-variant: normal;
    
    styleList = getStyleList(styleDict)
    
    W,H = svg.getSize()
    svg.draw(add_style('text',styleList)) 
        
    offsetx = 28
    offsety = 42
    x0 = W - 2*offsetx
    y0 = offsety
    yInter = 26
    xInter = 30
    
    x = x0
    y = y0
    for i in poet:
        for c in i:
            svg.draw(draw_text_only(x,y,text=c))
            y = y + yInter
        y = y0
        x = x - xInter
                
def drawStyleText(svg):
    text = '怡红快绿' #
    styleDict={}
    #styleDict['fill'] = 'black' 
    styleDict['font-family'] = 'Microsoft YaHei' 
    styleDict['font-size'] = '50px' 
     
    styleList = getStyleList(styleDict)
    
    W,H = svg.getSize()
    svg.draw(add_style('text',styleList)) 
          
    xInter = 60
    yInter = 60
    x0 = (W-xInter)/2
    y0 = (H-yInter)/2

    theta=0
    w,h = 2,2
    for i,c in enumerate(text):
        x = x0 + i%w * xInter
        y = y0 + i//w * yInter
        node = svg.draw(draw_text_only(x,y,text=c))
        svg.setNodeAttri(node, 'text-anchor', 'middle')
        svg.setNodeAttri(node, 'dominant-baseline', 'central')
        svg.setNodeAttri(node, 'fill', randomColor())
        str = 'rotate({},{},{})'.format(theta,x,y)
        svg.setNodeAttri(node, 'transform', str)
        #svg.draw(draw_circle(x,y,5,color='red'))
        theta += 90
    
def drawStyleText2(svg):
    text = 'Text rotation!'
    styleDict={}
    styleDict['fill'] = 'black' 
    styleDict['font-family'] = 'Consolas' 
    styleDict['font-size'] = '24px' 
     
    styleList = getStyleList(styleDict)
    
    W,H = svg.getSize()
    svg.draw(add_style('text',styleList)) 
        
    x0 = 10
    y0 = 30
    theta=0
    for _ in range(6):
        node = svg.draw(draw_text_only(x0,y0,text))
        if 1:
            svg.setNodeAttri(node, 'rotate', theta)
        else:
            str = 'rotate({},{},{})'.format(theta,x0,y0)
            svg.setNodeAttri(node, 'transform', str)
            svg.setNodeAttri(node, 'text-anchor', 'middle')
            svg.setNodeAttri(node, 'dominant-baseline', 'central')
            
        y0 += 25
        theta += 30
    
def main():
    #return drawText()

    file = gImageOutputPath + r'\text.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    #drawPoet(svg)
    #drawPoet2(svg)
    drawStyleText(svg)
    #drawStyleText2(svg)
    svg.close()
    
if __name__=='__main__':
    main()
    #cProfile.run('main()')