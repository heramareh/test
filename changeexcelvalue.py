#encoding=utf-8

from ParseExcel import ParseExcel

pe = ParseExcel("123.xlsx")
for sheet_name in pe.get_all_sheet_names():
    pe.get_sheet_by_name(sheet_name)
    for row in range(7,23,3):
        for col in range(6,18):
            num = pe.get_cell_content(row - 1, col)
            num = int(num) if num != None else None
            price = pe.get_cell_content(row, col)
            price = int(price) if price != None else None
            if num != None:
                pe.write_cell_content(row, col,num * price)
    for row in range(8,24,3):
        for col in range(6,18):
            num = pe.get_cell_content(row - 2, col)
            num = int(num) if num != None else None
            price = pe.get_cell_content(row, col)
            price = int(price) if price != None else None
            if num != None:
                pe.write_cell_content(row, col, num * price)
pe.save_file("234.xlsx")
