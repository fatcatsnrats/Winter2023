import matplotlib.pyplot as plt
import pandas as pd

bestTV = pd.read_csv(r'C:\Users\omara\Downloads\BestTV.csv')

fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Top four prime-time television shows')
fig.set_figwidth(17)

ax1.pie(bestTV['Television Show'].value_counts(), labels= bestTV['Television Show'].unique(), autopct='%1.1f%%')
ax2.bar(bestTV['Television Show'].unique(), bestTV['Television Show'].value_counts())
plt.show()