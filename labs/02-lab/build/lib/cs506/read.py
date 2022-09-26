import pandas as pd

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        matrix = []
        for row in csv_reader:
            matrix.append(row)
    print(csv_file_path , ", ", matrix)




s = "1"
int(s)
print(s)
            




    
    
    #raise NotImplementedError()
