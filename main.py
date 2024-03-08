from tkinter import filedialog
import pandas as pd

pd.set_option('display.max_columns', None)

file_path_Test = filedialog.askopenfilename()
file_path_Local = filedialog.askopenfilename()
TestData = pd.read_csv(file_path_Test, encoding='latin-1') # no separator
TestData.columns = ['Data']
LocalData = pd.read_csv(file_path_Local, encoding='latin-1') # no separator
LocalData.columns = ['Data']

#fileData = pd.read_csv(file_path, sep='~', encoding='latin-1', low_memory=False)

print(TestData[TestData.columns[0]].count())
print(LocalData[LocalData.columns[0]].count())
#SameData = TestData.loc[TestData.columns[0] != LocalData.columns[0]]
#print(SameData[SameData.columns[0]].count())

#LocalData = LocalData.sort_index(inplace=True)
#TestData = TestData.sort_index(inplace=True)

#TestData = TestData.reset_index(drop=True)
#LocalData = LocalData.reset_index(drop=True)
#print(TestData.columns[0] != LocalData.columns[0])

DiffData = pd.concat([TestData['Data'], LocalData['Data']], axis=1, keys=['Freeway', 'Legacy'])
#sep='+'

#print(TestData.loc[[100]])
#print(LocalData.loc[[100]])
DiffData = DiffData.loc[DiffData['Freeway'] != DiffData["Legacy"]]
print(DiffData)
DiffData.to_excel('Test.xlsx', index=False)









#MY DOCUMENTATION
'''
#NORMAL TEST
fileData['CurrentCode'] = fileData['CurrentCode'].astype('str')
#fileData['CurrentCode'] = fileData['CurrentCode'].str[:-2]
fileData = fileData.loc[fileData['CurrentCode'] != fileData['NewMap']]
fileData = fileData.loc[pd.isna(fileData['NewMap'])]
print("exporting now")
print(fileData[fileData.columns[3]].count())
#fileData.iloc[0:1000].to_excel('QuickTest.xlsx', index=False)
fileData.iloc[0:1000000].to_excel('EmptyMap.xlsx', index=False)
#fileData.iloc[0:1000000].to_excel('CurrNEnew.xlsx', index=False)
#fileData.iloc[1000000:2000000].to_excel('CurrNEnew2.xlsx', index=False)


# fileData cleanup
#fileData = fileData.loc[pd.isna(fileData['NewMap'])]
#fileData = fileData.loc[pd.isna(fileData['OldMap'])]
#fileData = fileData.loc[fileData['NewMap'] == "REJECT"]
#fileData = fileData.loc[fileData['CurrentCode'].astype('float') != fileData['NewMap'].astype('float')]
#print(fileData['CurrentCode'].astype('str').isin(fileData['NewMap'].astype('str')).value_counts())
#print(fileData.where(fileData['CurrentCode'].values==fileData['NewMap'].values).notna())
#fileData.iloc[0:1000000].to_excel('empty.xlsx', index=False)


for col in fileData.columns:
    print(col)
'''
'''
locatedRows = fileData.loc[fileData['New Material'] == 'Material not Recognised']
result = locatedRows.head(10000)
print(locatedRows)
'''

'''
fileData = fileData.loc[fileData['OldMap'] == 'REJECT']

#fileData.to_excel('CurrentCodeNotEqNewMap.xlsx', index=False)
print(fileData.iloc[0:1000])

'''
#MAYBE INSTEAD OF CONVERTING TO INT, JUST CONVERT THE CURRENT CODE TO STRING
#fileData = fileData[['CurrentCode', 'NewMap']].assign(NE=fileData.CurrentCode != fileData.NewMap)
#fileData = fileData.loc[fileData['CurrentCode'].eq(fileData['NewMap'])]
#fileData = fileData.loc[fileData['CurrentCode'] == fileData['NewMap'].astype('float')]
#fileData.to_excel('CurrEqOld.xlsx', index=False)
#print(fileData.iloc[0:500])
'''
fileData.iloc[0:1000000].to_excel('CurrentCodeNotEqNewMap.xlsx', index=False)
fileData.iloc[1000000:2000000].to_excel('CurrentCodeNotEqNewMap2.xlsx', index=False)
fileData.iloc[2000000:3000000].to_excel('CurrentCodeNotEqNewMap3.xlsx', index=False)
fileData.iloc[3000000:4000000].to_excel('RejectedOldComm4.xlsx', index=False)
fileData.iloc[4000000:5000000].to_excel('RejectedOldComm5.xlsx', index=False)
fileData.iloc[5000000:6000000].to_excel('RejectedOldComm6.xlsx', index=False)
fileData.iloc[6000000:7000000].to_excel('ConvertedFile7.xlsx', index=False)
fileData.iloc[7000000:8000000].to_excel('ConvertedFile8.xlsx', index=False)
fileData.iloc[8000000:9000000].to_excel('ConvertedFile9.xlsx', index=False)
fileData.iloc[9000000:10000000].to_excel('ConvertedFile10.xlsx', index=False)
'''


# fileData.loc[fileData['Construction'] == 'Not Set'].to_excel('ConstructionNotSet.xlsx', index=False)
# print(fileData.loc[fileData['Construction'] == 'Not Set'])
# fileData.loc[fileData['New Material'] == 'Not Fully Calculated'].to_excel('NFC_ConvertedData.xlsx', index=False)
# print('Not Fully Calculated exported')
# fileData.loc[fileData['New Material'] == 'Not Found'].to_excel('NF_ConvertedData.xlsx', index=False)
# print('Not Found')


# fileData.to_excel('WhatIsItMissing.xlsx', index=False)
# fileData.loc[fileData['What It Is'] == '   749'].to_excel('WhatIsItMissing.xlsx', index=False)
#fileData.drop(fileData['New Material'].str.contains('Not Found'))
#print(fileData.loc[fileData['New Material'].str.contains('Not Found')].iloc[0:10000])
#fileData.iloc[0:10000].to_excel('MadeFromTest.xlsx', index=False)
'''
fileData = fileData[(fileData['Material'].str.contains('Body:')) |
                    (fileData['Material'].str.contains('Bracelet:')) |
                    (fileData['Material'].str.contains('Earrings:')) |
                    (fileData['Material'].str.contains('Fabric1:')) |
                    (fileData['Material'].str.contains('Fabric:')) |
                    (fileData['Material'].str.contains('Hair Clip:')) |
                    (fileData['Material'].str.contains('Headband:')) |
                    (fileData['Material'].str.contains('Item1:')) |
                    (fileData['Material'].str.contains('Lace:')) |
                    (fileData['Material'].str.contains('Lens:')) |
                    (fileData['Material'].str.contains('Main:')) |
                    (fileData['Material'].str.contains('Necklace:')) |
                    (fileData['Material'].str.contains('Not Required:')) |
                    (fileData['Material'].str.contains('Outer:')) |
                    (fileData['Material'].str.contains('Ring:')) |
                    (fileData['Material'].str.contains('Shell1:')) |
                    (fileData['Material'].str.contains('Strap:')) |
                    (fileData['Material'].str.contains('Shell:'))]
fileData.loc[fileData['New Material'] == 'Material not Mapped'].to_excel('OnlyRootsMaterialnotMappedFromDump.xlsx', index=False)
'''
#fileData.loc[fileData['OldMap'] == 'REJECT'].to_excel('RejectedOldComm.xlsx', index=False)
