def  funca():
    a=3
    b=4
    print (a+b)
    print(eval('a+b'))






def newdemo():
    operatelist=['+','*']
    formatstring='%1dop%1d=%2d '
    for operator in operatelist:
        for a in range(1,10):
            print('\n')
            for b in range(a,10):
                curformat=formatstring.replace('op',operator)
                estr='a'+operator+'b'
                print(curformat%(a,b,eval(estr)),end ='')


if __name__=='__main__':
    
    #funca()
    newdemo()              
                
            






                      
                      
                      
