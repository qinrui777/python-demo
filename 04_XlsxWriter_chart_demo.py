# encoding: utf-8
# ref: https://xlsxwriter.readthedocs.io/chart_examples.html

import xlsxwriter

workbook  =xlsxwriter.Workbook('chart_column.xlsx')

worksheet  = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1 })

headings = ['Number','Batch1','Batch2']

data = [
        ['one','two','three','four','five'],
        [10,20,30,15,25],
        [30,60,70,50,40],
]

worksheet.write_row('A1',headings,bold) # 从A1开始，依次B2,C2...往后写入 headings的内容

worksheet.write_column('A2',data[0])
worksheet.write_column('B2',data[1])
worksheet.write_column('C2',data[2])

chart1 = workbook.add_chart({'type': 'column')

# chart2 = workbook.add_chart({'type': 'column', 'subtype': 'stacked'})
# chart3 = workbook.add_chart({'type': 'column', 'subtype': 'percent_stacked'})

# Configure the first series.
chart1.add_series({
    'name':       '=Sheet1!$B$1',   # 取B1的值：Batch1
    'categories': '=Sheet1!$A$2:$A$7',  # 取A2-A7 的名称
    'values':     '=Sheet1!$B$2:$B$7',  # 取B2-B7 的值
})

# Configure a second series. Note use of alternative syntax to define ranges.
chart1.add_series({
    'name':       ['Sheet1', 0, 2],       #取横坐标 0 ，纵坐标2的值： Batch2
    'categories': ['Sheet1', 1, 0, 6, 0], #取（横坐标1，纵坐标0）到（横坐标6，纵坐标0）的值
    'values':     ['Sheet1', 1, 2, 6, 2], #同上
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Results of sample analysis'})
chart1.set_x_axis({'name': 'Test number'})
chart1.set_y_axis({'name': 'Sample length (mm)'})

# Set an Excel chart style. 数值不同，对应不同的柱状颜色
chart1.set_style(11)

# Insert the chart into the worksheet (with an offset). 图形相对于 D2 偏移位置
worksheet.insert_chart('D2', chart1, {'x_offset': 0, 'y_offset': 0})

# worksheet.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 100})

workbook.close()