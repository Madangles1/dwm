import numpy as np
import pandas as pd
from apyori import apriori as apr2
from efficient_apriori import apriori as apr1
trans_data=pd.read_csv('Book1.csv',header=None)
dim=trans_data.shape

records=[]
for i in range(dim[0]):
    records.append([str(trans_data.values[i,j])  for j in range(dim[1])]  )
for r in records:
    while('nan' in r):
        r.remove('nan')


print("Apriori Algorithm")
print()
rules=apr1(records,min_support=0.5,min_confidence=0.5)
itemsets = apr2(records, min_support=0.5, min_confidence=0.5)
k=1


print("Itemset:")
for i in itemsets:
    
    for j in (list(list(i))[0]):
        print(j,end="")
    print()
print()  
print("Association Rules")    
for i in rules[1]:
    print(i)
 
