import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r'C:\Users\omara\Downloads\Cars.csv')

sns.regplot(x='Driving Speed (mph)', y='Fuel Efficiency (mpg)', data=df)

dfCovariance = round(df.cov(), 4)
dfCorrelation = round(df.corr(), 4)

print('\n' +'Covariance: \n' + str(dfCovariance))
print('\n' +'Correlation of Coefficient: \n' + str(dfCorrelation))

plt.show()