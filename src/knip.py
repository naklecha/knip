def sprint(*arg,end="\n",sep = " "):
    if(len(arg)==0):
        print(end=end,sep=sep)
        return
    for ele in arg[:len(arg)-1]:
        res = str(ele)
        if(len(res)>3000):
            print(res[:1000]+"\n"+"......\n"+"...... (%d characters)\n" %(len(res)-2000)+"......\n"+res[len(res)-1000:],end=sep)
        else:
            print(res,end=sep)
    res = str(arg[-1])
    if(len(res)>3000):
        print(res[:1000]+"\n"+"......\n"+"...... (%d characters)\n" %(len(res)-2000)+"......\n"+res[len(res)-1000:],end=end)
    else:
        print(res,end=end)
