import math  
def f(x):  
    return 4 * x**3 + 3 * x**2 - 18 * x - 7  
  
def derivative_f(x):  
    return 12 * x**2 + 6 * x - 18  
   
x = 0.0  
y = 0.0  
learning_rate = 0.001  
gradient = 0  
e = 0.00000001  
  
b1 = 0.9  
b2 = 0.995  
  
m = 0  
v = 0  
t = 0  

print('x\tf(x)\tgradient\n')

for i in range(10000):  
  
    print(x, y, gradient)  
    if(abs(gradient)>0.00001 and (abs(gradient)<0.0001)):  
        print("break at " + str(i))  
        break  
    else:   
        gradient = derivative_f(x)   
        t = t + 1  
        m = b1 * m + (1 - b1) * gradient  
        v = b2 * v + (1 - b2) * (gradient**2)  
        mt = m / (1 - (b1**t))  
        vt = v / (1 - (b2**t))    
        x = x - learning_rate * mt / (math.sqrt(vt) + e)   
        y = f(x)  