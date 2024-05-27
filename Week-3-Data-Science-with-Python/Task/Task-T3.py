import pandas as pd
import re

class PandasProgram:
    def __init__(self) -> None:
        self.df = pd.DataFrame({
            'company_code': ['Company', '001', '  ', '@001', 'Company/12'],
            'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022', '15/09/1997'],
            'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
            })
        
    def displayDataFrame(self):
        print("+---------------------------------------------------------------+")
        print(self.df)
        print("+---------------------------------------------------------------+")
        
    def isAlphabate(self,column):
        c = f"{column}_is_alpha"
        print("operation 1: Check whether alphabetic values are present.")
        self.df[c] = self.df[column].apply(lambda x: x.isalpha())
        self.displayDataFrame()
        self.df.drop(c,axis = 1,inplace=True)
    
    def isOnlyNumeric(self,column):
        c = f"{column}_is_numeric"
        print("Operation 2: Check whether only numeric values are present.")
        self.df[c] = self.df[column].apply(lambda x: x.isnumeric())
        self.displayDataFrame()
        self.df.drop(c,axis = 1,inplace=True)
    
    def isOnlySpace(self,column):
        c = f"{column}_is_space"
        print("Operation 3: Check whether only space is present in column.")
        self.df[c] = self.df[column].apply(lambda x: x.isspace())
        self.displayDataFrame()
        self.df.drop(c,axis = 1,inplace=True)
    
    def isOnlyNonalphanumeric(self,column):
        c = f"{column}_is_non_alphanumeric"
        print("Operation 4: Extract non-alphanumeric characters from the column.")
        self.df[c] = self.df[column].apply(lambda x: re.sub(r'\w', '', x))
        self.displayDataFrame()
        self.df.drop(c,axis = 1,inplace=True)

d = PandasProgram()
d.displayDataFrame()
column = "company_code"
d.isAlphabate(column)
d.isOnlyNumeric(column)
d.isOnlySpace(column)
d.isOnlyNonalphanumeric(column)
