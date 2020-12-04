from check import check_header_trail
from check import check_file_name
from manipulation import file_table_manipulation
from manipulation import meter_info_table_manipulation
from db_read_write import df_to_db

import os, time
import pandas as pd
import sqlite3

# Setting Variables
db_name='Gazprom_Energy_db'
file_table='Files'
info_table = 'Meter_Information'
read_file_path = 'incoming_data/'

def main():
    '''
    The main function used to take data from the directory and load into the sqlite database
    '''
    before = dict([(f, None) for f in os.listdir (read_file_path)])

    # Searching the directory for new files
    while 1:
        time.sleep (10)
        after = dict([(f, None) for f in os.listdir (read_file_path)])
        added = [f for f in after if not f in before]
        
        if added:
            for files in added: # For each of the files that have been added to the directory

                df = pd.read_csv(read_file_path+files,header=None)

                check_filename = check_file_name(files,df) # Checks the file to see if the filename matches the one in the file
                
                if check_filename != 'File Name Check Success':
                    print('The File Name Check was Unsuccessfull. \n The name of the file was {file_name}. \n In the file, the name was {name}.'.format(
                        name = check_filename,
                        file_name = files)
                        )
                else:
                    df = check_header_trail(df) # Checks the file for the header and the footer
                    file_df = pd.DataFrame()

                    file_df = file_table_manipulation(df,file_df) # Manipulates the datframe ready to add to file table
                    meter_info = meter_info_table_manipulation(df,file_df) # Manipulates the dataframe to add to meter info table
                    
                    file_table_response = df_to_db(file_df,db_name,file_table) # Inserts file dataframe to file table
                    print(file_table_response)
                    
                    if file_table_response =='Write to Files Unsuccessful': # If file df was corrupt or already existed in db table, dont write meter info
                        pass
                    else:
                        meter_info_table_response = df_to_db(meter_info,db_name,info_table) # Meter dataframe write to the meter info db table
                        print(meter_info_table_response)
        
        before = after # Continues to look for new files in the directory

if __name__ == '__main__':
    main()