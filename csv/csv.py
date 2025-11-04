import numpy as np

#only delimiter 
# data = np.genfromtxt('csv/dummy.csv', delimiter=',')

# print(data)



#with dtype
data = np.genfromtxt('csv/dummy.csv', delimiter=',', dtype=str)

print(data)




# with skip_header
# data = np.genfromtxt('csv/dummy.csv', delimiter=',', dtype=str, skip_header=1)

# print(data)

# Load data from CSV file
data = np.genfromtxt('csv/dummy.csv', delimiter=',', dtype=str, skip_header=1)

print(data)
