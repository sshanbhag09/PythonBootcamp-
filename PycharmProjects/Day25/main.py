# import csv
# temp=[]
# i=1
# with open("weather_data.csv") as data:
#     csv_data = csv.reader(data)
#     for row in csv_data:
#
#         if row[1]=="temp":
#             continue
#         temp.append(int(row[1]))
#     print(temp)
#
# import pandas
# data=pandas.read_csv("weather_data.csv")
# print(data)
#
# dict_data=data.to_dict()
# print(data["temp"].max())
# print(dict_data)
#
# dict_list=data["temp"].to_list()
# max=data["temp"].max()
# print(dict_data)
#
# print(data[data["temp"]== max])

import pandas as pd
dict={}
data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data.count())
greycount=data[data['Primary Fur Color']=='Gray']['Primary Fur Color'].to_list()
redcount=data[data['Primary Fur Color']=='Cinnamon']['Primary Fur Color'].to_list()
blackcount=data[data['Primary Fur Color']=='Black']['Primary Fur Color'].to_list()


seg={'color':['Gray','Red','Black'],
     'count':[len(greycount),len(redcount),len(blackcount)]}
df = pd.DataFrame(seg)

df.to_csv("squirrelcount.csv")
