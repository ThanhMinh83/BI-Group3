# file = open('datacf.txt')
# for cheese in file:
#     print(cheese)

# file = open('datacf.txt.txt')
# count = 0
# for line in file:
#     count = count + 1
# print('Line Count:', count)



import pandas as pd
import openpyxl
import pprint
wb = openpyxl.load_workbook('Data-Vinamilk.xlsx')
data= pd.read_excel('Data-Vinamilk.xlsx')
print(wb)
print(data.to_string())







