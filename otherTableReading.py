import os,sys
import pandas as pd, numpy as np
import datetime as dt
import time
import random
import xlrd

objectiveSheet = 'zdjgzjdxx'

nRows, nCols = workbook_query.sheet_by_name(objectiveSheet).nrows, workbook_query.sheet_by_name(objectiveSheet).ncols
colNames = []
workbook_queryDict = {}
for i in range(0, nCols):
    colNames.append(workbook_query.sheet_by_name(objectiveSheet).col_values(i)[0])
    workbook_queryDict[workbook_query.sheet_by_name(objectiveSheet).col_values(i)[0]] = \
        workbook_query.sheet_by_name(objectiveSheet).col_values(i)[1:]
data = pd.DataFrame(workbook_queryDict, columns=colNames)
            
print(data.shape)
lendingHelper = data.copy()


objectiveSheet = 'ktcxhtxl'

nRows, nCols = workbook_query.sheet_by_name(objectiveSheet).nrows, workbook_query.sheet_by_name(objectiveSheet).ncols
colNames = []
workbook_queryDict = {}
for i in range(0, nCols):
    colNames.append(workbook_query.sheet_by_name(objectiveSheet).col_values(i)[0])
    workbook_queryDict[workbook_query.sheet_by_name(objectiveSheet).col_values(i)[0]] = \
        workbook_query.sheet_by_name(objectiveSheet).col_values(i)[1:]
data = pd.DataFrame(workbook_queryDict, columns=colNames)

            
print(data.shape)
contactBook = data.copy()


objectiveSheet = '月报中机构类型'
# 之后 objectiveSheet 可以作为参数传进来。
# workbook_querydata = pd.DataFrame(workbook_query) 不能直接转化成df
nRows, nCols = workbook_query.sheet_by_name(objectiveSheet).nrows, workbook_query.sheet_by_name(objectiveSheet).ncols
colNames = []
workbook_queryDict = {}
for i in range(0, nCols):
    colNames.append(workbook_query.sheet_by_name(objectiveSheet).col_values(i)[0])
    workbook_queryDict[workbook_query.sheet_by_name(objectiveSheet).col_values(i)[0]] = \
        workbook_query.sheet_by_name(objectiveSheet).col_values(i)[1:]
data = pd.DataFrame(workbook_queryDict, columns=colNames)
            
print(data.shape)
dataCatagory = data.copy()
# 后续考虑如何try exception，容纳几种常见错误。
