#import csv
#
#with open('weather_data.csv')as file:
#    data =csv.reader(file)
#    temperature = []
#    for row in data:
#        if row[1]!='temp':
#            temperature.append(int(row[1]))
#    print(temperature)

import pandas
#data =pandas.read_csv('weather_data.csv')

# data_dict = data.to_dict()

# temp_list = data['temp'].to_list()
# print(round(sum(temp_list)/len(temp_list),2))

# print(data['temp'].mean())

# print(data['temp'].max())
# print(data)

# print(data[data.day=='Monday'])

# print(data[data.temp == data.temp.max()])

#data = {'students':['Ritik','Chintu','Raj'],'scores':[80,70,60]}
#
#pandas_data =pandas.DataFrame(data)
#
#print(pandas_data)

squirrel_data = pandas.read_csv('Squirrel_Data.csv')

black_fur = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])
grey_fur = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
red_fur = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])

fur_data = {'Color': ['grey', 'red', 'blck'], 'Count': [ grey_fur, red_fur,black_fur]}

fur_csv = pandas.DataFrame(fur_data)

fur_csv.to_csv('squirrel.csv')
