import pandas
#
# student_dict={
#     "student":["angela","james","lily"],
#     "score":[56,78,35]
# }
# data_frame=pandas.DataFrame(student_dict)
# print(data_frame )
#loop through a data frame
# for (key,value) in data_frame.items():
#     print(value )

# loop through a rows of a data frame
# for(index,row) in data_frame.iterrows():
#
#     if row.student=="angela":
#         print(row.score)
data=pandas.read_csv("C:/Users/nidas/PycharmProjects/day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

dict_1={row.letter:row.code for (index,row) in data.iterrows()}
print(dict_1)
ask_user=input("enter a word:").upper()
l1=[dict_1[code] for code in ask_user ]
print(l1)




