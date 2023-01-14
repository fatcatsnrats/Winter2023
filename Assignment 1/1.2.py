import matplotlib.pyplot as plt
import pandas as pd

computer = pd.read_csv(r'C:\Users\omara\Downloads\Computer.csv')

def graphs():
    plt.title('Hours of Personal Computer Use During One Week')
    plt.hist(computer['Hours'])
    plt.show()

def main():
    dMin = computer['Hours'].min()
    dQ1 = computer['Hours'].quantile(.25)
    dMed = computer['Hours'].median()
    dQ3 = computer['Hours'].quantile(.75)
    dMax = computer['Hours'].max()

    print('\n' + 'Minimum: ' + str(dMin))
    print('Q1: ' + str(dQ1))
    print('Median: ' + str(dMed))
    print('Q3: ' + str(dQ3))
    print('Maximum: ' + str(dMax))

    dRange = round(dMax - dMin, 3)
    dIQR = dQ3 - dQ1

    print('\n' + 'Range: ' + str(dRange))
    print('IQR: ' + str(dIQR), '\n')

    for x in computer['Hours']:
        if ((x < (dQ1 - ((3/2) * dIQR)))
            or (x > (dQ3 + ((3/2) * dIQR)))):
            print('Outlier: ' + str(x))

    dMean = round(computer['Hours'].mean(), 4)
    dVariance = round(computer['Hours'].var(), 4)
    dSTD = round(computer['Hours'].std(), 4)
    dCV = round(dSTD / dMean, 4)

    print('\n' + 'Mean: ' + str(dMean))
    print('Variance: ' + str(dVariance))
    print('Standard Deviation: ' + str(dSTD))
    print('Coefficient of Variation: ' + str(dCV) + '\n')

main()