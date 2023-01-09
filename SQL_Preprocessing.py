import mysql.connector
#-----------------------------------------------------------------------------------------------
def open_Connection():
    return mysql.connector.connect(user='root', 
                              password='12345',
                              host='127.0.0.1',
                              port=3307,
                              database='Oraghe_Mosharekat',
                              auth_plugin='mysql_native_password')
#-----------------------------------------------------------------------------------------------
def close_Connection(cnx):
    cnx.close()
#-----------------------------------------------------------------------------------------------
def checkTables():
    cnx = open_Connection()
    dropTables(cnx, 'Report_202')
    dropTables(cnx, 'Total_GL')
    dropTables(cnx, 'CTE_0')
    createTables(cnx)    
#-----------------------------------------------------------------------------------------------
def createTables(cnx):
    stmt = 'CREATE TABLE Report_202 ( Bran varchar(255), Amount varchar(255));'
    cursor = cnx.cursor()
    cursor.execute(stmt)     
    stmt = 'CREATE TABLE Total_GL ( Bran varchar(255), Amount varchar(255));'
    cursor = cnx.cursor()
    cursor.execute(stmt)      
    cnx.commit()
    stmt = 'CREATE TABLE CTE_0 ( Bran bigint, sumAmount bigint);'
    cursor = cnx.cursor()
    cursor.execute(stmt)      
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def dropTables(cnx, tableName):
    stmt = 'DROP TABLE IF EXISTS %s ;' %tableName
    cursor = cnx.cursor()
    cursor.execute(stmt)        
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def Preprocessing():
    checkTables()
#-----------------------------------------------------------------------------------------------
