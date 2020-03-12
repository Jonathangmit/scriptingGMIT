# Taken from online classes
# Call in numpy and matplotlib
import numpy as np 
import matplotlib.pyplot as plt
# Set values and number of points
x = np.linspace(0,4,50)
# Define functions
g = x**2
h = x**3
# Found how to get superscript and set x,y axis values from stack overflow
plt.xlim(0,5)
plt.ylim(0,70)
plt.plot(x,x,'g.', label ="first order f(x)=x")
plt.plot(x,g,'r.', label ="second order g(x)=$x^{2}$")
plt.plot(x,h,'y.', label ="third order h(x)=$x^{3}$")
plt.title("Function Values 0 to 4")
plt.xlabel(" x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()