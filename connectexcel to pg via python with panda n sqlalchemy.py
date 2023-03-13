from sqlalchemy import create_engine
import pandas as pd

#This will locate the excel file that will be transformed to a table.
Dataframe=pd.read_excel(r'C:\Users\ADMIN\Desktop\Cheesy Pesto Finance\financialsummary.xlsx',index_col=0,header=[0],sheet_name='financialsummary')

#This code locates the postgreSQL table in the local device.
engine = create_engine(r'postgresql://postgres:admin@localhost:5432/postgres', echo = True)

#This is the code that will create the new table with the data extracted from the excel file.
Dataframe.to_sql('cpfinance_new',engine,if_exists='replace')

