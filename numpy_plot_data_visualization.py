# Using a sample numpy array of my own and create a line plot and add any color to it.
# Import matplotlib.pyplot 
import matplotlib.pyplot as plt
import numpy as np

#Using a sample numpy array of your own and create a line plot and add any color to it.
np_row_data_1 = np.array([1, 2,3,4,5,6,7,8])
np_col_data_1 =np.array([10,20,30,40,50,60,70,80])
np_row_data_2 = np.array([2,4,6,8,10,12,14,16])
np_col_data_2 =np.array([10,20,30,40,50,60,70,80])
print("demo")

#create line plot
print("\n\n")
plt.plot(np_row_data_1, np_col_data_1, marker='P', color ='b', ls='dotted', linewidth = '2.0', label="Peter")
plt.plot(np_row_data_2, np_col_data_2, marker='p', color ='g', ls='dashdot', linewidth = '1.8', label="Rob")
plt.grid()  #Add grid view - clear understanding

#Add font, color and size to the label and title
bigFont = {'family':'fantasy','color':'blue','size':20}
smallFont = {'family':'cursive','color':'darkred','size':15}
plt.title("Students Learning Progress Report", fontdict=bigFont)
plt.xlabel("Weekly Progress", fontdict = smallFont)
plt.ylabel("Number of chapters learned",fontdict = smallFont)

#Add x-axis label - for clear understanding
tick_val = [2, 4, 6,8,10,12,14,16]
tick_lab = ['week1', 'week2', 'week3','week4','week5','week6','week7','week8']
plt.xticks(tick_val,tick_lab)

#Display legend(student name & represent line color) and show plt
plt.legend()
plt.show()
