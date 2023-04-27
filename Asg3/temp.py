import pandas as pd
from decimal import *

getcontext().prec = 16

df = pd.read_csv("training_data.txt", sep= "    ", names=["B","G","C","F"],engine='python')
total_values = len(df.index)
count_of_1_in_B = df["B"].value_counts()[1]
count_of_1_in_C = df["C"].value_counts()[1]
prob_B = [count_of_1_in_B/total_values, 1 - count_of_1_in_B/total_values]
prob_C = [count_of_1_in_C/total_values, 1 - count_of_1_in_C/total_values]

print(prob_B)
print(prob_C)

jp = df.groupby("B")['G'].value_counts()
conditional_probability_of_G_be_1_when_B_is_0 = jp[0][1]/sum(jp[0])
conditional_probability_of_G_be_1_when_B_is_1 = jp[1][1]/sum(jp[1])

data = [
    (1, Decimal(jp[1][1]/sum(jp[1])), Decimal(jp[1][0]/sum(jp[1]))),
    (0, Decimal(jp[0][0]/sum(jp[0])), Decimal(jp[0][1]/sum(jp[0])))
]
cpBG = pd.DataFrame(data,columns= ["B","G=1","G=0"])
cpBG.set_index("B",inplace=True)
print(cpBG)
jp =df.groupby(["B","C"])["G"].value_counts()