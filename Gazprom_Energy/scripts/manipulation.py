import pandas as pd
import datetime

def file_table_manipulation(origional_df,new_df):
    '''
    The function used to take the given file and creates a new dataframe in the structure needed for the file table
    '''
    new_df = new_df.append(origional_df.loc[0])
    new_df.columns = ['Record_Identifier','File_type_identifier', 'Company_ID','File_creation_date','File_creation_time','File_generation_number']
    
    new_df = new_df.drop(columns='Record_Identifier')
    new_df = new_df[['File_generation_number','File_type_identifier','Company_ID','File_creation_date','File_creation_time']]
    
    new_df['File_creation_date'] = new_df['File_creation_date'].astype(int) # setting the the coulmns to an int datatype
    new_df['File_creation_time'] = new_df['File_creation_time'].astype(int)

    date_time = str(datetime.datetime.now()) # Gets the date amd time and inserts into the pandas dataframe
    date_time = date_time.split('.')[0]
    new_df['Received_datetime'] = date_time
    
    return new_df

def meter_info_table_manipulation(origional_df,file_df):
    '''
    The function used to take the given file and creates a new dataframe in the structure needed for the meter info table
    '''
    origional_df = origional_df.drop(origional_df.index[0])
    origional_df = origional_df.drop(5, axis=1)

    new_df = origional_df.drop(columns=[0])

    new_df['File_generation_number'] = file_df['File_generation_number'].values[0]
    new_df.columns = ['Meter_Number','Measurement_Date','Measurement_Time','Consumption','File_generation_number']
    new_df['Measurement_Time'] = new_df['Measurement_Time'].astype(int) # Gets the date amd time and inserts into the pandas dataframe

    return new_df
