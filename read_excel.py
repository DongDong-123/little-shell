import xlrd


def read_excel(file_path):
    work_book = xlrd.open_workbook(file_path)
    all_sheet_name = work_book.sheet_names()  # return list
    return work_book, all_sheet_name


def get_sheel(work_book, name):
    # 根据索引获取sheet，从0开始
    sheet_content_by_index = work_book.sheet_by_index(0)

    # 根据sheet名字获取sheet
    sheet_content_by_name = work_book.sheet_by_name(name)
    return sheet_content_by_index


def get_row_col_num(sheet_content):
    """
    获取行、列的总数量
    :param sheet_content: sheet内容对象
    :return: int, 总的行、列数
    """
    return sheet_content.nrows, sheet_content.ncols


def get_info_by_row(sheet_content, row_num):
    """
    逐行读取所有数据
    :param sheet_content: sheet内容对象
    :param row_num: int 总行数
    :return: 生成器，一行数据组成的列表
    """
    for num in range(row_num):
        yield list(map(process_float, sheet_content.row_values(num)))


def get_info_by_col(sheet_content, col_num):
    """
    逐列读取所有数据
    :param sheet_content: sheet内容对象
    :param col_num: int 总列数
    :return: 生成器，一列数据组成的列表
    """
    for num in range(col_num):
        yield list(map(process_float, sheet_content.col_values(num)))


def get_info_by_cell(sheet_content, row_num, col_num):
    """
    按单元格逐行读取数据，(可选择按列)
    :param sheet_content: sheet内容对象
    :param row_num: int 总行数
    :param col_num: int 总列数
    :return: 生成器  包含单元格内容、类型元组的列表
    """
    for row in range(row_num):
        for col in range(col_num):
            sheet_cell_value = sheet_content.cell(row, col).value
            sheet_cell_value = list(map(process_float, [sheet_cell_value]))[0]
            sheet_value_type = get_cell_type(sheet_content, row, col)
            # sheet_cell_value = sheet_1.cell_value(row, col).encode('utf-8')
            # sheet_cell_value = sheet_1.row(row)[col].value.encode('utf-8')
            yield (sheet_cell_value, sheet_value_type)


def get_cell_type(sheet_content, row_index, col_index):
    """
    获取单元格内容的数据类型（ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error）
    :param sheet_content: sheet内容对象
    :param row_index: int 行索引
    :param col_index: int 列索引
    :return: str 单元格的类型
    """
    sheet_value_type = sheet_content.cell(row_index, col_index).ctype
    type_dict = {0: 'empty', 1: 'string', 2: 'number', 3: 'date', 4: 'boolean', 5: 'error'}
    return type_dict[sheet_value_type]


def process_float(parm):
    """
    判断是否为float类型，且为整数，整数则转换为int，
    :param parm: all type
    :return: 原数据或转换为int类型的整数
    """
    if isinstance(parm, float) and parm == int(parm):
        return int(parm)
    else:
        return parm


def main():
    # path = r"D:\Users\Dong\Desktop\test.xlsx"
    path = r"D:\Users\Dong\Desktop\桌面文本文档\2018杭州马拉松_男女前500.xlsx"
    work_book, sheet_names = read_excel(path)

    sheet_content = get_sheel(work_book, sheet_names[0])

    row_num, col_num = get_row_col_num(sheet_content)

    # 逐行读取数据
    read_info_by_row = get_info_by_row(sheet_content, row_num)  # 返回生成器
    for info in read_info_by_row:
        print(info)
    # 逐列读取数据
    read_info_by_col = get_info_by_col(sheet_content, col_num)  # 返回生成器
    # for info in read_info_by_col:
    #     print(info)
    cell_content = get_info_by_cell(sheet_content, row_num, col_num)
    # for info in cell_content:
    #     print(info)






if __name__ == "__main__":

    main()