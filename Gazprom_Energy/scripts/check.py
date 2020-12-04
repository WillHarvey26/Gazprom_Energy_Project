import pandas as pd

def check_header_trail(df):
    '''
    The function used to check the seleted file for the header and footer
    '''
    if 'HEADR' == df.values[0][0] and 'TRAIL' == df.values[-1][0]:
        df = df.drop(df.index[-1])
        return df
    else:
        pass

def check_file_name(file_name,df):
    '''
    The function used to check the name of the file matches the name provided inside the file
    '''
    name_in_file = df.values[0][-1]+ '.' + df.values[0][1]
    
    if file_name == name_in_file:
        return 'File Name Check Success'
    else:
        return name_in_file