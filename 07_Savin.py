# savefig("filepath.extention" , dpi = value , bbox_inches = "tight")
# DPI : dots per inch (img quality)
# bbox_inches : remove rounded space.

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [15 , 45 , 80 , 10 ,65]

plt.plot( x , y , color = 'blue' , marker = 'o')
plt.title("Simple line Graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.savefig("Line_plot.png" , dpi = 300 , bbox_inches = 'tight')
plt.show()