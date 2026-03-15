import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y = [ 30,70,10,20,90]

plt.plot(x,y , color = "green" , linestyle = "--" , linewidth = 2  , marker = "o" , label = '2026 sales data')

plt.title("Daily Record: ")
plt.xlabel("Day's")
plt.ylabel("Products seles")
plt.legend()
plt.grid() # background py box a jaty hain
 
# plt.savefig("Plot_Graph.png" , dpi = 300 , bbox_inches = 'tight')  # DPI : dots per inch (img quality)
                                                                   # bbox_inches : remove rounded space.
plt.show()