'''
#Q1
import numpy as np
a=np.random.randint(1,10,10)
print(a)
print(np.mean(a))

'''

#Q2



import numpy as np
a=np.random.randint(1,20,20)
print(a)
print(np.var(a))
print(np.std(a))



#Q3


import numpy as np
a=np.random.random((10,20))
b=np.random.random((20,25))
x=np.dot(a,b)
print(x)
print(np.sum(x))



#Q4
import numpy as np
import math
a=np.random.random((10,1))
print(a)
b=[]
for i in range (0,10):
    x=1/(1+math.exp(-(a[i,0])))
    b.append(x)
print(b)
'''