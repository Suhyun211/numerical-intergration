import math
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import csv

# f=lambda x: (R-u*math.cos(x))/(R**2+u**2-2*R*u*math.cos(x))**(3/2)
# R=10
a=0.65
L=0.26
h=0.026
x=0.4
y=0
z=0
def f_x(p, z):
    return -0.65*10**(-7)*(a*math.cos(p)*(z-h/(2*math.pi)*p)-(h)/(2*math.pi)*(y-a*math.sin(p)))/((x-a*math.cos(p))**2+(y-a*math.sin(p))**2+(z-h/(2*np.pi))**2)**1.5
def f_y(p, z):
    return -0.65*10**(-7)*(a*math.sin(p)*(z-h/(2*math.pi)*p)-(h)/(2*math.pi)*(x-a*math.sin(p)))/((x-a*math.cos(p))**2+(y-a*math.sin(p))**2+(z-h/(2*np.pi))**2)**1.5
def f_z(p, z):
    return -0.65*10**(-7)*(math.sin(p)*(y-a*math.sin(p))+math.cos(p)*(x-a*math.cos(p)))/((x-a*math.cos(p))**2+(y-a*math.sin(p))**2+(z-h/(2*np.pi))**2)**1.5



# def g(x,u):
#     return 
# ans=quad(f,0,2*np.pi)
# print(ans)

# u_array=np.arange(0,R-1,0.1)
z_array=np.arange(0,1,0.001)
xx=quad(f_x, 0,20*np.pi)[0]
yy=quad(f_y, 0,20*np.pi)[0]
zz=quad(f_z, 0,20*np.pi)[0]

print(xx,yy,zz)

integrals=[[z,math.sqrt((quad(f_x,0,20*np.pi, args=(z))[0])**2+(quad(f_y,0,20*np.pi, args=(z))[0])**2+(quad(f_z,0,20*np.pi, args=(z))[0])**2)] for z in z_array]

# with open('move_0.40.csv','w', newline='') as file :

#     write = csv.writer(file)
#     write.writerows(integrals)
x=np.linspace(0,L, 200)
x,y=zip(*integrals)
plt.plot(x,y)
plt.show()
