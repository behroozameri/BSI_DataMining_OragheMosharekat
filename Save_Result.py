import pandas as pd
import numpy as np
from openpyxl import load_workbook
import mysql.connector
import os
from os.path import dirname
#-----------------------------------------------------------------------------------------------
def open_Connection():
    return mysql.connector.connect(user='root', 
                              password='12345',
                              host='127.0.0.1',
                              port=3307,
                              database='Oraghe_Mosharekat',
                              auth_plugin='mysql_native_password')
#-----------------------------------------------------------------------------------------------
def save_CTE_0(writer):
    cnx = open_Connection()
    cursor = cnx.cursor()
    query = """SELECT Bran, SumAmount FROM CTE_0 ORDER BY Bran""" 
    cursor.execute(query)
    rows = []
    header = ['Bran','Sum_202']
    rows.append(header)
    for (Bran, SumAmount) in cursor:
        row = []
        row.append(Bran)
        row.append(SumAmount)
        rows.append(row)
    cursor.close()
    cte_0 = pd.DataFrame(rows)
    cte_0.to_excel(writer, sheet_name = 'SUM_202', index = False, header = False)
#-----------------------------------------------------------------------------------------------
def save_CTE_1(writer):
    cnx = open_Connection()
    cursor = cnx.cursor()
    query = """SELECT Bran, Amount FROM CTE_1 ORDER BY Bran""" 
    cursor.execute(query)
    rows = []
    header = ['Bran','GL']
    rows.append(header)
    for (Bran, Amount) in cursor:
        row = []
        row.append(Bran)
        row.append(Amount)
        rows.append(row)
    cursor.close()
    cte_1 = pd.DataFrame(rows)
    cte_1.to_excel(writer, sheet_name = 'GL', index = False, header = False)
#-----------------------------------------------------------------------------------------------
def save_CTE_2(writer):
    cnx = open_Connection()
    cursor = cnx.cursor()
    query = """SELECT Bran, Sum_202, Amount_GL, Sum_202_GL FROM CTE_2 ORDER BY Bran""" 
    cursor.execute(query)
    rows = []
    header = ['Bran','Sum_202', 'Amount_GL', 'Sum_202_GL']
    rows.append(header)
    for (Bran, Sum_202, Amount_GL, Sum_202_GL) in cursor:
        row = []
        row.append(Bran)
        row.append(Sum_202)
        row.append(Amount_GL)
        row.append(Sum_202_GL)
        rows.append(row)
    cursor.close()
    cte_2 = pd.DataFrame(rows)
    cte_2.to_excel(writer, sheet_name = 'Result', index = False, header = False)
#-----------------------------------------------------------------------------------------------
def save_CTE_5(writer):
    cnx = open_Connection()
    cursor = cnx.cursor()
    query = """SELECT Bran, SumAmount FROM CTE_5 ORDER BY Bran""" 
    cursor.execute(query)
    rows = []
    header = ['Bran','Sum_202']
    rows.append(header)
    for (Bran, SumAmount) in cursor:
        row = []
        row.append(Bran)
        row.append(SumAmount)
        rows.append(row)
    cursor.close()
    cte_3 = pd.DataFrame(rows)
    cte_3.to_excel(writer, sheet_name = 'Not_in_GL', index = False, header = False)
#-----------------------------------------------------------------------------------------------
def save_CTE_6(writer):
    cnx = open_Connection()
    cursor = cnx.cursor()
    query = """SELECT Bran, Amount FROM CTE_6 ORDER BY Bran""" 
    cursor.execute(query)
    rows = []
    header = ['Bran','GL']
    rows.append(header)
    for (Bran, Amount) in cursor:
        row = []
        row.append(Bran)
        row.append(Amount)
        rows.append(row)
    cursor.close()
    cte_4 = pd.DataFrame(rows)
    cte_4.to_excel(writer, sheet_name = 'Not_in_202', index = False, header = False)
#-----------------------------------------------------------------------------------------------
def Save():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dirname(dir_path) + '\\files\output.xlsx'
    writer = pd.ExcelWriter(dir_path, engine = 'openpyxl')
    save_CTE_0(writer)
    save_CTE_1(writer)
    save_CTE_2(writer)
    save_CTE_5(writer)
    save_CTE_6(writer)
    writer.close()
#-----------------------------------------------------------------------------------------------
