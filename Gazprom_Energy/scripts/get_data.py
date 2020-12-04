import pandas as pd
from db_read_write import select_distinct_from_db
from db_read_write import select_with_condition_from_db

# Setting values
db_name='Gazprom_Energy_db'
validity = 'not valid'

while validity == 'not valid':
    # Gets input from the user via the commandline/console
    user_input= input('Please choose which requirement you would like to fulfill by typing the number followed by enter.\n\n1 - Get number of meters in the db \n2 - Get all data for given meter \n3 - Get the amount of files in the db \n4 - Get the latest uploaded filename \n')

    if user_input == '1':
        # Setting relivant values
        table_name='Meter_Information'
        value='Meter_Number'
        rows = select_distinct_from_db(db_name,table_name,value)
        count = 0
        
        for row in rows:
            count = count + 1 # Counts number of rows returned

        print('There is {number_of_meters} meter(s) in the database'.format(number_of_meters=count))
        print(rows)
        validity = 'valid' # Sets validity to valid meaning that the loop will complete
    
    elif user_input == '2':
        # Setting relivant values
        table_name='Meter_Information'
        value='Meter_Number'
        columns='Meter_Number,Measurement_Date,Measurement_Time,Consumption,File_generation_number'

        # Gets the user to input the specific meter nuber that is to be queried
        user_defined_number = input('\nPlease type the exact meter number followed by enter to find the data held on that meter\n')
        rows = select_with_condition_from_db(db_name,table_name,value,columns,user_defined_number)
        df = pd.DataFrame(rows,columns=['Meter_Number','Measurement_Date','Measurement_Time','Consumption','File_generation_number'])
        if df.empty == True:
            print('The file {user_file} could not be found in the db'.format(user_file = user_defined_number))
            validity = 'not valid' # Sets validity to invalid meaning that the loop will not complete
        else:
            print(df)
            validity = 'valid' # Sets validity to valid meaning that the loop will complete

    elif user_input == '3':
        # Setting relivant values
        table_name='Files'
        values='File_generation_number'
        rows = select_distinct_from_db(db_name,table_name,value)
        count = 0
        
        for row in rows:
            count = count + 1 # Counts number of rows returned

        print('There is {number_of_files} file(s) that has been recieved and is in the database'.format(number_of_files=count))
        print(rows)
        validity = 'valid' # Sets validity to valid meaning that the loop will complete

    elif user_input == '4':
        # Setting relivant values
        table_name='Files'
        values='File_generation_number,Received_datetime'

        rows = select_distinct_from_db(db_name,table_name,values)
        df = pd.DataFrame(rows,columns=['File_generation_number','Received_datetime'])
        df['Received_datetime'] = df['Received_datetime'].astype('datetime64[ns]')
        
        # Gets the latest time from the retrieved results
        latest_datetime = df.Received_datetime.max()
        latest_file = df.loc[df['Received_datetime'] == latest_datetime, 'File_generation_number']
        latest_file = latest_file.values[0]

        print('The latest file is {file} which was recived at {datetime}'.format(
            file = latest_file,
            datetime = latest_datetime))
        validity = 'valid' # Sets validity to valid meaning that the loop will complete

    else:
        print ('Please select either 1,2,3 or 4 followed by the enter key')
        validity = 'not valid' # Sets validity to invalid meaning that the loop will not complete