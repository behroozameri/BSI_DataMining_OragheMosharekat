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
def make_data_CTE_0():
    cnx = open_Connection()
    stmt = 'INSERT INTO CTE_0 (Bran, sumAmount) SELECT CAST(Bran AS UNSIGNED) AS Bran, SUM(CAST(Amount AS UNSIGNED)) AS Amount FROM Report_202 GROUP BY Bran;'
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()  
#-----------------------------------------------------------------------------------------------
def make_data_CTE_1():
    cnx = open_Connection()
    stmt = 'INSERT INTO CTE_1 (Bran, Amount) SELECT CAST(Bran AS UNSIGNED) AS Bran, CAST(Amount AS UNSIGNED) AS Amount FROM Total_GL;'
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def Process():
    make_data_CTE_0()
    make_data_CTE_1()
#-----------------------------------------------------------------------------------------------
