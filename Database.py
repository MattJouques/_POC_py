#!/usr/bin/python
#
#    POC - Database Connectivity
#
#    @author: Matt Jouques
#

# Configuration
dbConfig = {
  'user': 'development',
  'password': 'd3v3l0pm3nt',
  'host': 'alpha.local',
  'database': 'development',
  'raise_on_warnings': True,
  'buffered': True,
}

# Dependencies
import mysql.connector
from mysql.connector import errorcode

# Main
try:
    db = mysql.connector.connect(**dbConfig)                                        # Setup Database connection using information from config
    cursor = db.cursor()                                                            # prepare a cursor object using cursor() method
    cursor.execute("SELECT VERSION()")                                              # execute SQL query using execute() method.
    data = cursor.fetchone()                                                        # Fetch a single row using fetchone() method.
    print "Database version : %s " % data
    
    # Check to see if a table exists
    stmt = "SHOW DATABASES LIKE 'development1';"
    cursor.execute(stmt)
    result = cursor.fetchone()
    if result:
        print "Database Exists"                                                     # there is a Database named "development"
    else:
        print "Database does not exist"                                             # there are no databases named "development"
    
    # Create testTables
    from Database_Tables import TABLES                                              # Import create tables statements from file
    for name, ddl in TABLES.iteritems():                                            # Iterate through the items in the Tables List
        try:
            print("Creating table {}: ".format(name))
            cursor.execute(ddl)                                                     # Execute the command
        except mysql.connector.Error as err:                                        # Trap for errors
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:                        # Check for table exists error
                print("already exists.")
            else:
                print(err.msg)                                                      # Display other messages
        else:
            print("OK")   
    
    # Drop Employee Tables
    from Database_Tables import DROPTABLES                                          # Import drop tables statements from file
    cursor.execute('SET foreign_key_checks = 0;')                                   # Remove the foreign key constraint to enable tables to be dropped
    for name, ddl in DROPTABLES.iteritems():                                        # Iterate through the items in the DropTables list
        try:
            print("Dropping Table {}: ".format(name)) 
            cursor.execute(ddl)                                                     # Execute the command
        except mysql.connector.Error as err:                                        # Trap for errors
            print "Error occurred: %s " % err                                       # Display the errors
    cursor.execute('SET foreign_key_checks = 1;')                                   # Re-enable the foreign key constraint
    
    # Get Table column details
    from mysql.connector import FieldType
    cursor.execute("SELECT * FROM _POC_py")                                         # Change the cursor
    for i in range(len(cursor.description)):                                        # Iterate through the cursor
        print("Column {}:".format(i+1))                                             # Set the Column Header
        desc = cursor.description[i]                                                # Get the Cursor Description
        print("  column_name = {}".format(desc[0]))
        print("  type = {} ({})".format(desc[1], FieldType.get_info(desc[1])))
        print("  null_ok = {}".format(desc[6]))
        print("  column_flags = {}".format(desc[7]))
        
    # Write the column names into a list
    colNames = []                                                                   # Set the list object
    for i in range(len(cursor.description)):                                        # Iterate through the cursor
        desc = cursor.description[i]                                                # Get the Cursor Description
        colNames.append(desc[0])                                                    # Append the name to the list
    print ','.join(colNames)
    
    # Add row to table
    import time
    sql = "INSERT INTO _POC_py VALUES (null, 'test item 1', 'test item 2', '%s')" % time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        cursor.execute(sql)
        print("affected rows = {}".format(cursor.rowcount))
        db.commit()
    except mysql.connector.Error as err:                                        # Trap for errors
        print "Error occurred: %s " % err                                       # Display the errors
    
    # Add multiple rows to table via a list
    
    
    # Update rows in table
    
    
    # Add Data to the remaining table
    #sql = "insert into _POC_py VALUES(null, 'Mars City', 'MAC', 'MARC', 1233)"

except mysql.connector.Error as err:                            # Capture any errors
    print(err)
else:
    #cursor.close()                                              # Close the cursor
    db.close()                                                  # Close the Database connection
