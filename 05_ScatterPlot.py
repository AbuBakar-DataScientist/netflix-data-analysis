# Relations between data
# use to find the co_relation between two  veriables
# e.g : Advertising budget VS sales 

import matplotlib.pyplot as plt

hours_study = [1,2,3,4,5,6,7]
marks = [30,40,50,60,70,90,95]

plt.scatter(hours_study,marks , color = 'green' , marker='d' , label = 'Studen Data')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Relation between study time and score:')
plt.legend()
plt.grid(True)


# plt.savefig("Scatter_Graph.png" , dpi = 300 , bbox_inches = 'tight')  # DPI : dots per inch (img quality)
                                                                   # bbox_inches : remove rounded space.
plt.show()