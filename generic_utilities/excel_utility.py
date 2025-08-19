import xlrd

path = r'C:\Users\Ramya\PycharmProjects\POM-A12-Aug18-2025\external_files\data.xlsx'


def excel_data(sheet):
    workbook = xlrd.open_workbook(path)             ## book object
    worksheet = workbook.sheet_by_name(sheet)       ## sheet object
    rows = worksheet.get_rows()                     ## generator object
    header = next(rows)

    data = {}
    for ele in rows:
        data[ele[0].value] = ele[1].value

    return data





































































