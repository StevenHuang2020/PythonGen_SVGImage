
from svgBasic import *
from svgFile import *
import re

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
    poet.append('过故人庄')
    poet.append('孟浩然')
    poet.append('故人具鸡黍，邀我至田家。')
    poet.append('绿树村边合，青山郭外斜。')
    poet.append('开轩面场圃，把酒话桑麻。')
    poet.append('待到重阳日，还来就菊花。')

    styleDict={}
    styleDict['fill'] = 'red' 
    styleDict['font-family'] = 'KaiTi' #'Microsoft YaHei' 
    styleDict['font-size'] = '12px' 
    #font-style: normal; font-variant: normal;
    
    styleList=''
    for i in styleDict:
        styleList = styleList + (i+':' + styleDict[i] + ';')
    
    W,H = svg.svgSize()
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
    poet.append('红楼梦')
    poet.append('可叹停机德，')
    poet.append('堪怜咏絮才。')
    poet.append('玉带林中挂，')
    poet.append('金簪雪里埋。')

    styleDict={}
    styleDict['fill'] = 'red' 
    styleDict['font-family'] = 'Microsoft YaHei' 
    styleDict['font-size'] = '24px' 
    #font-style: normal; font-variant: normal;
    
    styleList=''
    for i in styleDict:
        styleList = styleList + (i+':' + styleDict[i] + ';')
    
    W,H = svg.svgSize()
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
        
def main():
    file = gImageOutputPath + r'\poem.svg'
    H,W=200,200
    svg = SVGFileV2(file,W,H,border=True)
    #drawText()
    #drawPoet(svg)
    drawPoet2(svg)
    svg.close()
    
if __name__=='__main__':
    main()