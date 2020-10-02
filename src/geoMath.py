#python3 Steven
#geometry math
import numpy as np 

def getLineParam(pt1,pt2):
    """get line slope and bias"""
    slope,bias = None,None
    if pt1[0] != pt2[0]:
        slope = (pt1[1]-pt2[1])/(pt1[0]-pt2[0])
        bias = pt1[1] - slope*pt1[0]
    return slope, bias

def main():
    x = [1,2]
    y = [3,4]
    
    print(getLineParam(x,y))
    
if __name__=='__main__':
    main()