import numpy as np 

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, room in enumerate(areas) :
    print("room " + str(index) +  ": " + str(room))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    index += 1
    print("room " + str(index) + ": " + str(area))


# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for h in house:
    print("the" , h[0] , "is" , h[1], "sqm")


# for k, v in world.items():
#     #iterating over dictionaries



# for val in np.nditer(my_array):

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for x, y in europe.items():
    print("the capital of", x, "is", y)

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np.nditer(np_height):
    print(x, "inches")

# For loop over np_baseball
for a in np.nditer(np_baseball):
    print(a)

# for lab, row in brics.itterrows():
#     brics.loc[lab, "name_length"] = len(row["country"])
# print(brics)
# lab(row lab)
#row(row data)
#row["capital"]
# brics["name_length"] = brics["country"]. apply(len)
# print(brics)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": "+ str(row["cars_per_cap"]))


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)