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
    stmt = 'INSERT INTO CTE_0 (Bran, SumAmount) SELECT CAST(Bran AS UNSIGNED) AS Bran, SUM(CAST(Amount AS UNSIGNED)) AS Amount FROM Report_202 GROUP BY Bran;'
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()  
#-----------------------------------------------------------------------------------------------
def make_data_CTE_1():
    cnx = open_Connection()
    stmt = 'INSERT INTO CTE_1 (Bran, Amount) SELECT CAST(Bran AS UNSIGNED) AS Bran, CAST(Amount AS SIGNED) AS Amount FROM Total_GL;'
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def make_data_CTE_2():
    cnx = open_Connection()
    stmt = '''INSERT INTO CTE_2 (Bran, Sum_202, Amount_GL, Sum_202_GL) 
                SELECT A.Bran , A.SumAmount, B.Amount, ( A.SumAmount + B.Amount) AS res 
                FROM CTE_0 AS A
                JOIN CTE_1 AS B
                ON A.Bran = b.Bran;'''
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def make_data_CTE_3():
    cnx = open_Connection()
    stmt = '''INSERT INTO CTE_3 (Bran) 
                SELECT Bran FROM CTE_0
                EXCEPT 
                SELECT Bran FROM CTE_1;'''
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def make_data_CTE_4():
    cnx = open_Connection()
    stmt = '''INSERT INTO CTE_4 (Bran) 
                SELECT Bran FROM CTE_1
                EXCEPT 
                SELECT Bran FROM CTE_0;'''
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def make_data_CTE_5():
    cnx = open_Connection()
    stmt = '''INSERT INTO CTE_5 (Bran, SumAmount) 
                SELECT * FROM CTE_0
                WHERE Bran IN 
                (SELECT * FROM CTE_3);'''
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def make_data_CTE_6():
    cnx = open_Connection()
    stmt = '''INSERT INTO CTE_6 (Bran, Amount) 
                SELECT * FROM CTE_1
                WHERE Bran IN
                (SELECT * FROM CTE_4);'''
    cursor = cnx.cursor()
    cursor.execute(stmt)   
    cnx.commit()
#-----------------------------------------------------------------------------------------------
def Process():
    make_data_CTE_0()
    make_data_CTE_1()
    make_data_CTE_2()
    make_data_CTE_3()
    make_data_CTE_4()
    make_data_CTE_5()
    make_data_CTE_6()
#-----------------------------------------------------------------------------------------------
