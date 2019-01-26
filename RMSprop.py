import math  
def f(x):  
    return 4 * x**3 + 3 * x**2 - 18 * x - 7  
  
def derivative_f(x):  
    return 12 * x**2 +6 * x - 18  
  
  
x = 0.0  
y = 0.0  
learning_rate = 0.001  
gradient = 0  
e = 0.00000001  
sum = 0.0  
d = 0.9   
Egt = 0  
Edt = 0   
delta = 0  
  
print('x\tf(x)\tgradient\n')

for i in range(100000):  
  
    print(x, y, gradient)  
    if(abs(gradient)>0.00001 and (abs(gradient)<0.0001)):  
        print("break at "+str(i))  
        break  
    else: 
        gradient = derivative_f(x)  
        Egt = d * Egt + (1 - d) * (gradient**2)  
        x = x - learning_rate * gradient / math.sqrt(Egt + e)  
        y = f(x)
