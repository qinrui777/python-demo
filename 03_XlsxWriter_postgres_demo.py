# encoding: utf-8
import psycopg2
import xlsxwriter

# please have a look at README.md 
# demo4: 

#connect to the db, ref:http://initd.org/psycopg/docs/module.html
con = psycopg2.connect(
    host = '127.0.0.1',
    database = 'db_demo_1',
    user = 'postgres',
    password = '123456',
    port = 5432
)

#cursor
cur = con.cursor()

#data is exist, execute query
cur.execute("select * from users")

result = cur.fetchall()
print (result.__class__)  # type: list

workbook = xlsxwriter.Workbook('/Users/ruqin/Desktop/postgres_demo1.xlsx')
worksheet = workbook.add_worksheet('queryResult')

row = 0
col = 0

cell_format = workbook.add_format()
cell_format.set_shrink()  //缩小字体以适应
# cell_format.set_bold()
# cell_format.set_font_color('red')
# cell_format.set_text_wrap() 自动换行
# cell_format.set_text_justlast()
# cell_format.set_align('justify')

bold =  workbook.add_format({'bold':True})

# Write some data headers.
worksheet.write('A1', 'ID', bold)
worksheet.write('B1', 'NAME', bold)
worksheet.write('C1', 'AGE', bold)
worksheet.write('D1', 'ADDRESS', bold)

for j in range(len(result)):
    # print (j)
    # print (result[j])

    for k in range(len(result[j])):
        # print (k)
        # print (result[j][k])
        worksheet.write(j+1,k,result[j][k],cell_format)

workbook.close()

#commit the transcation
con.commit()

#close the cursor
cur.close()

#close the connection
con.close()
