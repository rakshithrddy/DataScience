import pandas as pd
import numpy as np

# # counts = pd.Series([632,456,224,643])
# # print(counts)
# # print(counts.index)
# # print(counts.values)
#
# paint = pd.Series([645,5668,533,567], index=['red','blue','green','yellow'])
# print(paint)
# paint.index.name = 'color'
# paint.name = 'petroleum products'
# print(paint.name)
# print(paint.index.name)
#
# print(paint[[name.endswith('paint') for name in paint.index]])
# print([name.endswith('paint') for name in paint.index])
# print(paint[0])
# print(np.log(paint))
# print(paint>1000)
#
# paint1_dict = {'red':474, 'blue':4789, 'green':47838, 'yellow':49874}
# pd.Series(paint1_dict)
data = pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient':[1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria',
    'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})
# print(data)
# print(data[['phylum','value','patient']])
# print(data.columns)
# print(data.patient) #prints values without header
# print(type(data.value))
# print(data[['value']]) #prints the values with header
# print(data.loc[0]) # to print out a single row from the dataframe
# print(data.head(2))
# print(data.tail(3))
# print(data.shape)
# vals = data.values #copy only the values from the dataframe to vals
# print(vals)
# vals[5] = 0 # assign the 5th row values to 0
# print(vals)
# print(data)

# data['year'] = 2013
# print(data)
# data.treatment = 1
# print(data)
# pd.set_option("display.max_columns", 4)
mb = pd.read_csv("C:\\Users\\Rakshith\\PycharmProjects\\Data Science\\product.csv")
mb1 = pd.read_table("C:\\Users\\Rakshith\\PycharmProjects\\Data Science\\product.csv")
print(mb1)
