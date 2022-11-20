
import pandas as pd
#Ejercicio 1

print("Ejercicio 1")
print("-"*75)

df = pd.read_csv("Automobile_data.csv")
df.head(5)

print(df.head)



df = pd.read_csv("Automobile_data.csv")
df.tail(5)

print(df.tail)




#Ejercicio 2

print("Ejercicio 2")
print("-"*75)

df1 = pd.read_csv("Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})


df1.to_csv("Automobile_data.csv")
print (df1)
#Ejercicio 3

print("Ejercicio 3")
print("-"*75)

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
df

print(df)

#Ejercicio 4

print("Ejercicio 4")
print("-"*75)

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
toyotaDf

print(toyotaDf)

#Ejercicio 5

print("Ejercicio 5")
print("-"*75)

import pandas as pd
df = pd.read_csv("Automobile_data.csv")
df['company'].value_counts()

#Ejercicio 6

print("Ejercicio 6")
print("-"*75)

df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['company','price'].max()

print(priceDf)

#Ejercicio 7

print("Ejercicio 7")
print("-"*75)

df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby('company')
mileageDf = car_Manufacturers['company','average-mileage'].mean()
mileageDf

print(mileageDf)

#Ejercicio 8

print("Ejercicio 8")
print("-"*75)

carsDf = pd.read_csv("Automobile_data.csv")
carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
print(carsDf.head(5))

#Ejercicio 9

print("Ejercicio 9")
print("-"*75)

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)

japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(japaneseCars)

carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
carsDf

print(carsDf)

#Ejercicio 10

print("Ejercicio 10")
print("-"*75)

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
carsDf

print(carsDf)