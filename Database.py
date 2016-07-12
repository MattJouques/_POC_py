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
}

# Dependencies
import mysql.connector

# Main
try:
    db = mysql.connector.connect(**dbConfig)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")
    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print "Database version : %s " % data
except mysql.connector.Error as err:
    print(err)
else:
    db.close()
