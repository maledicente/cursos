soma=lambda a,b: a+b
mul=lambda a,b,c: (a+b)*c

#print(soma(2,5))
#print(mul(2,5,3))
#print((lambda a,b: a+b)(3,5))
r=lambda x,func: x+func(x)
res=r(2,lambda x: x*x)
print(res)