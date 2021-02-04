#importing module
from matplotlib import pyplot as plt
#plotting first strip
plt.plot([2,3],[5,5],color='darkorange',linewidth=50)
#making the middle strip
plt.plot([2,3],[3,3],color='blue',linewidth=50)
#making third strip
plt.plot([2,3],[1,1],color='green',linewidth=50)
#The X-axis is same for all just tweaking the Y-axis
#showing the plot
plt.show()
#let's run this