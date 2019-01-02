import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(2015,1,1)
end = dt.datetime.now()

# Saved a local copy of TSLA.csv so we don't need a web call everytime
#df = web.DataReader("TSLA", 'yahoo',start,end)
#df.reset_index(inplace=True)
#df.set_index("Date", inplace=True)
##df = df.drop("Symbol", axis=1)
#df.to_csv("TSLA.csv")

df = pd.read_csv('TSLA.csv', parse_dates = True, index_col = 0)

df['100ma'] = df['Adj Close'].rolling(window=100).mean()

# Test commit


df.plot()
plt.show()



