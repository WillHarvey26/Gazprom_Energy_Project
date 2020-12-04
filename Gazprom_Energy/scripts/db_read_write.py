import pandas as pd
import sqlite3

def df_to_db(df,db_name,table_name):
    '''
    The function used to write a dataframe to a table
    '''
    try:
        conn = sqlite3.connect('{db}.db'.format(db = db_name)) # Conect to db
        df.to_sql(table_name, conn, if_exists='append', index = False) # Writes to db table specifed
        conn.close() # Close connection to db
        return 'Write to {table} table Success'.format(table = table_name)
    except:
        return 'Write to {table} Unsuccessful'.format(table = table_name)

def select_distinct_from_db(db_name,table_name,value):
    '''
    The function used to select distinct values from the db
    '''
    conn = sqlite3.connect('{db}.db'.format(db = db_name)) # Conect to db
    
    c = conn.cursor()
    c.execute('''SELECT DISTINCT {value} FROM {table};'''.format(table=table_name, value=value))

    rows = c.fetchall()
    conn.close()
    return rows

def select_with_condition_from_db(db_name,table_name,value,columns_to_return,condition):
    '''
    The function used to select values with a condition from the db
    '''
    conn = sqlite3.connect('{db}.db'.format(db = db_name)) # Conect to db
    c = conn.cursor()
    c.execute('''SELECT {columns} FROM {table} WHERE {value} = '{condition}';'''.format(table=table_name,
        value=value,
        columns= columns_to_return,
        condition = condition))
    
    rows = c.fetchall()
    conn.close()
    return rows