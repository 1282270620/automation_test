from openpyxl import load_workbook

def read_test_case_data(file_path):
    param_list = []
    total_list = []
    data_dict = {}
    workbook = load_workbook(file_path)
    worksheet = workbook.active
    
    columns = worksheet.max_columns
    for i in range(0,columns):
        title = worksheet[1][i].value
        param_list.append(title)
        
    rows = workbook.max_rows
    for row in range(2,rows+1):
        data_list = []
        for col in range(0,columns):
            cell_value = worksheet[row][col].value
            if cell_value is None:
                cell_value = " "
            data_list.append[cell_value]
        total_list.append(data_list)
    data_dict["param_list"] = param_list
    data_dict["total_list"] = total_list
    
    return data_dict