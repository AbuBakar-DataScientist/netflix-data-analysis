# multiple graph ko single window py show krny kelye use hota
# e.g : 1st_graph show the shop sales & 2nd_show the shop expensise
# we can draw multiple graph on sigle canva

import matplotlib.pyplot as plt

fig , ax = plt.subplots(1,2 , figsize = (10 , 5)) # 10_width , 5_height
#( fig , ax 2 ( figurs & axes ) obejct return krta hai ..inko koi bhi name dy sakty hain 
# these like varibales.


x = [1,2,3,4,5]
y = [10 , 20 ,15 , 19 , 25]

ax[0].plot(x,y , color = 'green' ,  marker = 'd')
ax[0].set_title("Line Chart")

ax[1].bar(x,y , color = 'blue')
ax[1].set_title('Bar Chart')

fig.suptitle('Comparison of line chart and bar chart')

plt.tight_layout() # full screen py adjust kr dy ga sab charts ko automaticaly.

# plt.savefig("Sub_Graph.png" , dpi = 300 , bbox_inches = 'tight')  # DPI : dots per inch (img quality)
                                                                   # bbox_inches : remove rounded space.
plt.show()