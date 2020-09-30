#%/usr/bin/python
import mysql.connector
from mysql.connector import Error

def mysql_connect():
  mydb = mysql.connector.connect(host='localhost',
                                      database='twitter_project',
                                      user='root',
                                      password='')
  if(mydb):
    return mydb
  else:
    print('connection is unsuccessfull')



