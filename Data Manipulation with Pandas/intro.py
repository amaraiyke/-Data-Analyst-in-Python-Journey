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

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

homelessness = []

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)


dogs["height_m"] = dogs["height_cm"] / 100 #adding a new column in a different measure named height_m

print(dogs)

bmi_lt_100 = dogs[dogs["bmi"] < 100]

bmi_lt_100_height = bmi_lt_100.sort_values("height_cm", ascending = False)
bmi_lt_100_height[["name", "height_cm", "bmi"]]

homelessness = []

# Add total col as sum of individuals and family_members
homelessness["total"] =homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of total that are individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness)

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending = False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)