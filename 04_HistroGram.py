# Data kitna spread hai across ranges.
# jab data ko group mein show krna hota
# e.g : 100 students ky number hain..in mein 50 sy 70 waly kitny hain, OR less then 50 kitny hain etc

import matplotlib.pyplot as plt

marks = [50,40,76,98,45,67,87,34,56,78,45,65,35,64]

plt.hist(marks , bins=5 , color='purple' , edgecolor= 'black')
plt.xlabel('Score Rage')
plt.ylabel('Number of students')
plt.title('Score Distribution of studetns')


# plt.savefig("HistroGram_Graph.png" , dpi = 300 , bbox_inches = 'tight')  # DPI : dots per inch (img quality)
                                                                   # bbox_inches : remove rounded space.
plt.show()