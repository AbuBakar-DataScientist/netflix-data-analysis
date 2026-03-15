# y ham jab 4 5 logon ka data compare krna hota hai
# e.g : kis ny kitni Matplotloib sekh li.

import matplotlib.pyplot as plt

regions = ['North' , 'South' , 'East' , 'West']
revenue = [1500 , 1100 , 1770 , 1900]

plt.pie(revenue, labels=regions, autopct='%1.1f%%',colors=['gold', 'skyblue', 'lightgreen', 'coral'])

plt.title('Revenue Contribution By Region')

#  plt.savefig("Pie_Graph.png" , dpi = 300 , bbox_inches = 'tight')  # DPI : dots per inch (img quality)
                                                                   # bbox_inches : remove rounded space.
plt.show()