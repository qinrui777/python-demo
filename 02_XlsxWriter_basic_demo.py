
import xlsxwriter

# https://xlsxwriter.readthedocs.io/tutorial01.html

workbook = xlsxwriter.Workbook('/Users/ruqin/Desktop/expense01.xlsx')
# workbook = xlsxwriter.Workbook('expense01.xlsx')

worksheet = workbook.add_worksheet()

bold =  workbook.add_format({'bold':True})

money = workbook.add_format({'num_format': '$#,##0'})

worksheet.write('A1','Item',bold)
worksheet.write('B1','Cost',bold)

expenses = (
    ['Rent',1000],
    ['Gas', 100],
    ['Food',300],
)

item1  = expenses[1]

# print (expenses.__class__)  type:tuple  
# print (item1.__class__)  type: list

# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row
for item,cost in (expenses):
    worksheet.write(row,col,item)
    worksheet.write(row,col + 1, cost)
    row += 1

#write a total using a formula
worksheet.write(row,0,'Total',  bold)
worksheet.write(row,1,'=SUM(B2:B4)' , money)

workbook.close()
