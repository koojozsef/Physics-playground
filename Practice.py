import matplotlib.pyplot as plt
import numpy as np
import math
from math import e

timeline = np.arange(0,1000,1.0)
values = timeline*0

for i in timeline:
    
    values[int(i)]= (e ** (i*.01*1j)).imag

plt.plot(timeline,values)
plt.ylabel('some numbers')
plt.show()