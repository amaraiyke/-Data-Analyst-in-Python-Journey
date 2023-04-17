import pandas as pd
dogs = []

dogs.head() #displays first five rows of a DataFrame

dogs.shape #attribute that shows the number of rows followed by the number of columns

dogs.describe() #method that computes the summary statistics, quick overview

dogs.values #contains data values in a 2D array

dogs.columns #contains column names

dogs.index #contains row numbers or row names

#Sorting and Subsetting


dogs.sort.values("weight_kg") #lightest dog at the top

dogs.sort.values("weight_kg", ascending = False) #lightest dog at the bottom

dogs.sort.values(["weight_kg", "height_cm"], ascending = [True, False]) #sorting first by weight with the lightest at the top and then by height when weight is the same, tallest to shortest

dogs["name"] #zoom in a column

dogs[["breed", "height_cm"]] #same as:

cols_to_subset = ["breed", "height_cm"]
dogs[cols_to_subset]

dogs["height_cm"] > 50  #true or false result

dogs[dogs["height_cm"] > 50] #subset to get actual rows and columns

dogs[dogs["breed"] == "Labrador"] #filter dogs that are labradors

dogs[dogs["date_of_birth"] < "2015-01-01"] #filter for dogs before 2015

#Multiple Conditions

is_lab = dogs["breed"] == "Labrador"

is_brown = dogs["color"] == "Brown"

dogs[is_lab & is_brown]

dogs[ (dogs["breed"] == "Labrador") & (is_brown = dogs["color"] == "Brown") ]

#Filter on multiple values of a categorical variable using .isin() method

is_black_or_brown = dogs["color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]

