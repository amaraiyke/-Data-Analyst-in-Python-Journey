#select columns with double square brackets [[]]

## select rows with slices brics[1:4] , 2nd, 3rd and 4th rows are selected

#loc (label-based)
#iloc(integer-position based)

brics.loc[["RU"]]  #selects row about Russia

brics.loc[["RU"], ["country", "capital"]]  #selects row about Russia with specified rows to keep

brics.loc[:, ["country", "capital"]] #selects all rows but only specifies two columns


brics.iloc[[1,2,3]]

brics.iloc[[1,2,3], [0,1]]


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars["country"])

# Print out country column as Pandas DataFrame
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country", "drives_right"]])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Print out observation for Japan
print(cars.loc["JPN"])

# Print out observations for Australia and Egypt
print(cars.iloc[[1, 6]])

# Print out drives_right value of Morocco
print(cars.loc[["MOR"]])

# Print sub-DataFrame
print(cars.loc[["RU", "MOR"], ["country", "drives_right"]])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, "drives_right"])

# Print out drives_right column as DataFrame
print(cars.loc[:, ["drives_right"]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ["cars_per_cap", "drives_right"]])
