

import random

def  computepie():
    totalcount=10000000  #总试验数量
    curcount=0           #当前试验数量
    incirclecount=0      #落在圆中的数量
    while(curcount<totalcount):
        x=random.random()
        y=random.random()  #在边长为1.0正方形区域内随机生成点
        curcount+=1
        if(x*x+y*y<1.0):   
            incirclecount+=1  #判断所生成的点是否在正方形内
    print ("\n total=%ld  incircle=%ld "%(curcount,incirclecount))
    print ("\n pei=%f" %(incirclecount/curcount*4))


if __name__=="__main__":
    for i in range(1,5):
         computepie()
    
            
            
    
