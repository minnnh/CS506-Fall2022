def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    result_2D = []
    result_list = []

    with open( csv_file_path, newline = '') as file:
        result_list = list(csv.reader(file))

    for i in result_list:
        buffer = []
        for ele in i:
            if ele.isnumeric():
                ele = int(ele)
            buffer.append(ele)
        
        result_2D.append(buffer)
    return result_2D
    
    #raise NotImplementedError()
