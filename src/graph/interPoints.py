class GetLineSegInterPoint():
    def __init__(self, line1, line2):
        self.interPoint = self.getCrossPoint(line1,line2)

    def inSegment(self, p, line1,line2):
        """"check the cross point is on line segment """
        
        if p[0] >= min(line1[0][0],line1[1][0]) and p[0] <= max(line1[0][0],line1[1][0]):
            if p[0] >= min(line2[0][0],line2[1][0]) and p[0] <= max(line2[0][0],line2[1][0]):
                 if p[1] >= min(line1[0][1],line1[1][1]) and p[1] <= max(line1[0][1],line1[1][1]):
                    if p[1] >= min(line2[0][1],line2[1][1]) and p[1] <= max(line2[0][1],line2[1][1]):
                        return True
        return False
        
        '''
        if line1[0][0] == line1[1][0]:#如果line竖直
            if  p[1] > min(line1[0][1],line1[1][1]) and p[1] < max(line1[0][1],line1[1][1]):
                #if p[1] >= min(line2[0][1],line2[1][1]) and p[1] <= max(line2[0][1],line2[1][1]):
                if p[0] >= min(line2[0][0],line2[1][0]) and p[0] <= max(line2[0][0],line2[1][0]):
                    return True
        elif line1[0][1] == line1[1][1]:#如果line水平
            if p[0] > min(line1[0][0],line1[1][0]) and p[0] < max(line1[0][0],line1[1][0]):
                #if p[0] >= min(line2[0][0],line2[1][0]) and p[0] <= max(line2[0][0],line2[1][0]):
                if p[1] >= min(line2[0][1],line2[1][1]) and p[1] <= max(line2[0][1],line2[1][1]):
                    return True
        else:
            if p[0] > min(line1[0][0],line1[1][0]) and p[0] < max(line1[0][0],line1[1][0]):
                #line为斜线时，line2有可能竖直也有可能水平，所以对x和y都需要检查
                if p[1] >= min(line2[0][1],line2[1][1]) and p[1] <= max(line2[0][1],line2[1][1]) and p[0] >= min(line2[0][0],line2[1][0]) and p[0] <= max(line2[0][0],line2[1][0]):
                    return True
        return False
        '''
        
    def getCrossPoint(self,line1,line2):
        """line[0]: line start point,line[1]: stop point"""
        def getLinePara(line):
            a = line[0][1] - line[1][1]
            b = line[1][0] - line[0][0]
            c = line[0][0] *line[1][1] - line[1][0] * line[0][1]
            return a,b,c

        '''计算交点坐标，此函数求的是line1中被line2所切割而得到的点，不含端点'''
        a1,b1,c1 = getLinePara(line1)
        a2,b2,c2 = getLinePara(line2)
        d = a1* b2 - a2 * b1
        p = [0,0]
        if d == 0: #d为0即line1和line2平行
            return None

        p[0] = round((b1 * c2 - b2 * c1)*1.0 / d,2)#工作中需要处理有效位数，实际可以去掉round()
        p[1] = round((c1 * a2 - c2 * a1)*1.0 / d,2)
        p = tuple(p)
        if self.inSegment(p,line1,line2):
            return p
        return None


def test():
    line1 = [[0,0],[1,0]]
    line2 = [[0.5,1],[0.5,-1.5]]
    
    p = GetLineSegInterPoint(line1,line2).interPoint
    print('p=',p)

def main():
    test()
    
if __name__ == '__main__':
    main()
