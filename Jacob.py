import _thread
from threading import Thread
import time
a=0
b=0
c=0
itear=int(1e5)

def fun1(x2,x3):
    global a
    for i in range(itear):
        print("a=", a)
        a = -1/5+2/5*x2-0.6*x3

def fun2(x1,x3):
    global b
    for i in range(itear):
        print("b=", b)
        b= 2/9+1/3*x1-1/6*x3

def fun3(x1,x2):
    global c
    for i in range(itear):
        print("c=",c)
        c= -3/7+2/7*x1-1/7*x2

t1=Thread(target=fun1,args=(b,c,))
t2=Thread(target=fun2,args=(a,c,))
t3=Thread(target=fun3,args=(a,b,))

t1.start()
t2.start()
t3.start()

#for i in range(itear):
    # a=fun1(b,c)
    # b=fun2(a,c)
    # c=fun3(a,b)
    # 创建两个线程
    # try:
    #     _thread.start_new_thread(fun1,(b,c,) )
    #     _thread.start_new_thread(fun2,(a,c,))
    #     _thread.start_new_thread(fun3,(a,b,))
    # except:
    #     print("Error: 无法启动线程")

print(a,b,c)