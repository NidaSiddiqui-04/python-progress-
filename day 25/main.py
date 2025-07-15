# with open("weather_data.csv") as weather:
#     data=weather.readlines()
#     print(data)
#
#
# import csv
#
#
# with open("weather_data.csv") as weather_data:
#     data=csv.reader(weather_data)
#     temperature=[]
#     for row in data:
#         print(row)
#         if row[1]!="temp":
#             temperature.append((row[1]))
#     print(temperature)


import pandas
# data=pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"].to_list())
# print(data.columns)
# # print(data.to_dict())
# # datum=data["temp"].to_list()
# # print(datum)
# # print(sum(datum)/len(datum))
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # print(data["temp"].min())
# # #get data in column
# # print(data["day"])#here day is key
# # print(data.day)#here day is used as attributes
# # get data in row
# print(data[data["temp"]==data.temp.max()])
# monday=data[data.day=="Monday"]
# temp_feh=(monday.temp*(9/5))+32
# print(temp_feh)
#
# # data = {'row_1': [3, 2, 1, 0], 'row_2': ['a', 'b', 'c', 'd']}
# # datum=pandas.DataFrame.from_dict(data, orient='index')
# # print(datum.to_dict())
#
# #create a dataframe from scratch
# data_dict={
#            "Students":["Nida","Sahil","Sarwar"]
#            ,"Score":[29,58,90]
#            }
# data=pandas.DataFrame.from_dict(data_dict,orient="index",columns=[1,2,3])
# data.to_csv("my_file.csv")
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
no_gray=data[data["Primary Fur Color"]=="Gray"]
print(len(no_gray))
no_cinnamon=data[data["Primary Fur Color"]=="Cinnamon"]
print(len(no_cinnamon))
# no_cinnamon=data["Primary Fur Color"]=="Cinnamon"
# print(no_cinnamon.count())
no_black=data[data["Primary Fur Color"]=="Black"]
print(len(no_black))
data_dict={
    "Fur Color":["Gray","Cinnamon","Black"]
    ,"counts":[len(no_gray),len(no_cinnamon),len(no_black)]
}

file=pandas.DataFrame.from_dict(data_dict)
file.to_csv("Squirrel_count.csv")
