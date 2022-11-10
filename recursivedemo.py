
def loopsum(num):   #这个用循环来计算 1+2+ ....num
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum

def recursive_sum(num): #这个用递归来计算 1+2+ ....num 
    if(num>1):
        return num+recursive_sum(num-1)   #如果大于1，这样调用
    else:
        return num                        #如果等于1，直接返回结果
        
  


def  hanio(layer,fromc,toc,midc):        #汉诺塔问题 递归解决函数

     if(layer==1):
         print ("\n %d %c-->%c"%(layer,fromc,toc))
         #如果是最小圆盘，直接移动就可以
     else:                                            
         hanio(layer-1,fromc,midc,toc)
         #先把上边的n-1个盘，移动到中间柱子
         print ("\n %d %c-->%c"%(layer,fromc,toc))
         #再把最下边的盘，移动到目标柱子
         hanio(layer-1,midc,toc,fromc)
         #再把上边的n-1个盘，从中间柱子，移动到目标柱子


if __name__=="__main__":

    hanio(2,'A','C','B')    
    #print ("sum of loop is %d" % loopsum(100))
    #print ("sum of recursive of %d" % recursive_sum(100))       
           
