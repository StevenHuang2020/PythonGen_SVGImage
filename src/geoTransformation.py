#python3 Steven
#geotransformaion operation for coordiantes
import numpy as np 

def translationMatrix(x,y,toPoint): 
    """translation matrix, for moving shape"""
    a = np.stack(([x,y]))
    one = np.array([[toPoint[0]], [toPoint[1]]]) 
    #one = np.array([toPoint[0], toPoint[1]]).T.reshape((2,1))
    
    M=one
    for i in range(a.shape[1]-1):
        M = np.concatenate((M,one),axis=1)
    
    res = a + M
    # print('a=',a)
    # print('M=',M)
    # print('res=',res)
    return res[0][:],res[1][:]

def rotationMatrix(x,y,theta):  
    """rotation matrix with (0,0)"""
    a = np.stack(([x,y]))
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c,-s],[s,c]])
    res = np.dot(R, a)
    #return np.dot(R, a)
    return res[0][:],res[1][:]

def rotationMatrixCenter(x,y,rotPoint,theta):
    """rotation with rotation point"""
    transPt = (-1*rotPoint[0],-1*rotPoint[1])
    x,y = translationMatrix(x,y,transPt) #move to (0,0)
    x,y = rotationMatrix(x,y,theta)      #rotation
    
    transPt = (rotPoint[0],rotPoint[1])
    return translationMatrix(x,y,transPt) #move to rotPoint
   
def zoomMatrix(x,y,z=2):
    return x*z,y*z

def zoomMatrixCenter(x, y, zooPoint, z=2):
    transPt = (-1*zooPoint[0], -1*zooPoint[1])
    x,y = translationMatrix(x,y,transPt) #move to (0,0)
    x,y = zoomMatrix(x,y,z=z)  #zoom
    
    transPt = (zooPoint[0],zooPoint[1])
    return translationMatrix(x,y,transPt) #move to zooPoint


def main():
    x = [1,2]
    y = [3,4]
    translationMatrix(x,y,(1,2))
    #translationMatrix(x,y,(-1.5,-3.5))
    
if __name__=='__main__':
    main()