import mysql.connector
#-----------------------------------------------------------------------------------------------
def open_Connection():
    try:
        return mysql.connector.connect(user='root', 
                                password='12345',
                                host='127.0.0.1',
                                port=3307,
                                database='Oraghe_Mosharekat',
                                auth_plugin='mysql_native_password')
    except:
        create_DataBase()
        return mysql.connector.connect(user='root', 
                                password='12345',
                                host='127.0.0.1',
                                port=3307,
                                database='Oraghe_Mosharekat',
                                auth_plugin='mysql_native_password')
#-----------------------------------------------------------------------------------------------
def create_DataBase():
    cnx = mysql.connector.connect(user='root', 
                                password='12345',
                                host='127.0.0.1',
                                port=3307,
                                database='mysql',
                                auth_plugin='mysql_native_password')
    stmt = 'CREATE DATABASE Oraghe_Mosharekat ;'
    cursor = cnx.cursor()
    cursor.execute(stmt)      
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def close_Connection(cnx):
    cnx.close()
#-----------------------------------------------------------------------------------------------
def checkTables():
    cnx = open_Connection()
    dropTables(cnx, 'Report_202')
    dropTables(cnx, 'Total_GL')
    dropTables(cnx, 'CTE_0')
    dropTables(cnx, 'CTE_1')
    createTables(cnx)    
#-----------------------------------------------------------------------------------------------
def createTables(cnx):
    stmt = 'CREATE TABLE Report_202 (Bran varchar(255), Amount varchar(255));'
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()  
    stmt = 'CREATE TABLE Total_GL (Bran varchar(255), Amount varchar(255));'
    cursor = cnx.cursor()
    cursor.execute(stmt)      
    cnx.commit()
    stmt = 'CREATE TABLE CTE_0 (Bran bigint, sumAmount bigint);'
    cursor = cnx.cursor()
    cursor.execute(stmt)      
    cnx.commit()
    stmt = 'CREATE TABLE CTE_1 (Bran bigint, Amount bigint);'
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
