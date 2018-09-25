import pandas as pd
import quandl
import math
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import time as t
from openpyxl.workbook import Workbook

style.use('ggplot')
def tabular_data(x):
    '''
    In this module,first the data will be stored in df by using quandl which is used to extract data from internet.
    Then it will import the data in excel file using openpyxl module from df from where user can see the desired stock
    database.

    '''    

    
    df = quandl.get(x, authtoken="Hnvy8vdThdeDyybit-9o")
    df.to_excel('test.xlsx', sheet_name='sheet1', index=False)



def Graphical_data(x):
    '''
    In this module,data will be displayed in graphical form using matplotib module.
    
    '''
    
    df = quandl.get(x, authtoken="Hnvy8vdThdeDyybit-9o")
    df['Adj. Open'].plot()
    df['Adj. High'].plot()
    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price')
    return plt
    
def Predicted_data(x):
    '''
    In this module,linear Regression theory has been used to predict the stock prices.
    Here, the train set size is 0.9 and test set size on which predicton has to be made
    is 0.1
    error will also be displayed
    and then predicted data will be displayed in graphical form

    '''
    df = quandl.get(x, authtoken="Hnvy8vdThdeDyybit-9o")
    
    df =df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

    df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']
    df['HL_change'] = (df['Adj. High']-df['Adj. Low'])/df['Adj. Low']
    df = df[['Adj. Close', 'PCT_change', 'HL_change','Adj. Volume']]
    
    
    df.fillna(value=-99999, inplace=True)
    forecast_col = 'Adj. Close'
    forecast_out = int(math.ceil(.01*len(df)))
    df['label'] = df[forecast_col].shift(-forecast_out)

    

    X = np.array(df.drop(['label'],1))
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

   
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]

    
    df.dropna(inplace=True)
    y = np.array(df['label'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    
    clf = LinearRegression()
    clf.fit(X_train, y_train)
    forecast_set = clf.predict(X_lately)
    df['Forecast'] = np.nan

    last_date = df.iloc[-1].name
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day

    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += 86400
        df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]





    
    df['Forecast'].plot()
    
    plt.legend(loc=4)
    plt.xlabel('Date')
    plt.ylabel('Price')

    return plt


if __name__ == '__main__':
    tabular_data(x)
    Graphical_data(x)
    Predicted_data(x)
