Gazprom_Energy PROJECT

    *incoming_data Directory*
        The 'incoming_data' directory is needed for when new files arrive.
        When the new files are wrote to the project they are to be wrote into the incoming_data directory where the script will be watching for new files.

    *Database*
        The database has been created with DDL and has been done so with Sqlite3.
        This has been done becuase of the requirement specifiying the project to be portable.
        The project is portable as there isno need for a server to host the database when using Sqlite3 meaning that the file is stored locally.

    *scripts Directory*
        The 'Scripts' directory contains all of the Python scripts that needed to exicute the project and are split into different sections
        Each of the scripts are wrote in python and are all necessary for the running of the program.
        The 'check.py' script is used by the 'main.py' file to be able to check a df for a header and footer in the file to make sure it is a complete file.
        The 'check.py' file is alsoused by the 'main.py' file to be able to check that the filename matches the one in the header (This was not a requirment but could see some use if the file was to be wrongly named or accidentally re-named).
        The 'manipulation.py' file is used by the 'main.py' file to perform actions on the file to be able to insert into the relevant tables.
        The 'db_read_write.py' file is used by the 'main.py' fileas well as the 'get_data.py'file to both write and query the database.
        The 'main.py' file is what is used to run the project to be bale to watch for new files, check the files, put them into the correct format and insert them into the database.
        The 'get_data.py' file is what is used to query the database. This script is independent of the 'main.py' file and uses the 'db_read_write.py' file to search for data.

    RUNNING THE PROJECT
        To run project the 'main.py' file has to be run to be able to search the directory for any new files, this will automatically insert these into the sqlite3 db.
        To be able to query the data the 'get_data.py' file has to be run. This will need some user input through the commandline to be able to determine what queries want to be displayed annd returned in the console.

THANK YOU FOR READING

PROJECT COMPLETED BY WILLIAM HARVEY