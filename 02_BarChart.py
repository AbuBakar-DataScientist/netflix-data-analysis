# islye use hota hai jab kisi data ko compair krna hota hai...
# e.g : daily sales kitni hoi.

import matplotlib.pyplot as plt

product = ['A' , 'B' , 'C' , 'D']
sales = [950 , 1700 , 600 , 1200]

plt.bar(product , sales , color = 'orange' , label = 'Sales 2026')
plt.xlabel("product's")
plt.ylabel("Sale's")
plt.title('Product sale Comparison:')
plt.legend()



# plt.savefig("Bar_Graph.png" , dpi = 300 , bbox_inches = 'tight')  # DPI : dots per inch (img quality)
                                                                   # bbox_inches : remove rounded space.
plt.show()